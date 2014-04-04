#!/usr/bin/env python

from bs4 import BeautifulSoup
import codecs
import contextlib
import datetime
import glob
import hashlib
import html5lib
import jinja2
import markdown
import multiprocessing
import ntpath
import operator
import os
import posixpath
import re
import shutil
import stat
import subprocess
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'template')
CACHE_DIR = os.path.join(ROOT_DIR, 'cache')


def remove_readonly(fn, path, excinfo):
    if not os.path.isdir(path):
        return
    if fn is os.rmdir:
        os.chmod(path, stat.S_IWRITE)
        os.rmdir(path)
    elif fn is os.remove:
        os.chmod(path, stat.S_IWRITE)
        os.remove(path)


def delete_output_directory():
    shutil.rmtree(OUTPUT_DIR, onerror=remove_readonly)
    assert not os.path.isdir(OUTPUT_DIR)


def copy_static_files():
    for source_dir in ['css', 'js']:
        source = os.path.join(TEMPLATE_DIR, source_dir)
        destination = os.path.join(OUTPUT_DIR, source_dir)
        shutil.copytree(source, destination)
    for filename in ['favicon.ico']:
        source = os.path.join(TEMPLATE_DIR, filename)
        destination = os.path.join(OUTPUT_DIR, filename)
        shutil.copyfile(source, destination)


class TemplateLoader(object):
    def __init__(self, path=TEMPLATE_DIR):
        self.template_loader = jinja2.FileSystemLoader(searchpath=path)
        self.template_env = jinja2.Environment(loader=self.template_loader)

    def get_template(self, path):
        return self.template_env.get_template(path)


def build_index(loader):
    template = loader.get_template('index.html')
    output_text = template.render(date=datetime.date.today().isoformat(),
                                  active_section="index")
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as f_out:
        f_out.write(output_text)


class Category(object):
    def __init__(self, path):
        self.path = path
        self.load_root_meta_yaml()
        self.load_games()

    def load_root_meta_yaml(self):
        root_meta_yaml_path = os.path.join(self.path, 'meta.yaml')
        assert os.path.isfile(root_meta_yaml_path), \
            'path %s does not have a meta.yaml file' % self.path
        with open(root_meta_yaml_path) as f_in:
            root_meta_yaml = yaml.load(f_in)
        self.category_title = root_meta_yaml['category title']
        self.category_name = os.path.basename(self.path)

    def load_games(self):
        paths = [subpath for subpath in glob.glob(os.path.join(self.path, "*"))
                 if os.path.isdir(subpath) and
                 len(os.listdir(subpath)) > 0]
        self.games = sorted([Game(path) for path in paths], key=operator.attrgetter('name'))


class Game(object):
    required_files = [['description.html', 'description.htm', 'description.md'],
                      ['meta.yaml'],
                      ['summary.html', 'summary.htm', 'summary.md']]

    def __init__(self, path):
        self.path = path
        self.game_id = os.path.basename(path)
        for filenames in self.required_files:
            fullpaths = [os.path.join(self.path, filename) for filename in filenames]
            assert any(os.path.isfile(fullpath) for fullpath in fullpaths), \
                'Could not find any file %s. One is required.' % fullpaths
        self.load_meta_yaml()
        self.load_summary()
        self.load_description()
        self.images = [filepath for filepath in glob.glob(os.path.join(self.path, '*'))
                       if any(filepath.endswith(ext) for ext in ['.jpg', '.gif', '.png'])]

    def __str__(self):
        return "{game_id=%s}" % (self.game_id, )

    def load_meta_yaml(self):
        with open(os.path.join(self.path, 'meta.yaml')) as f_in:
            self.meta_yaml = yaml.load(f_in)
        self.validate_meta_yaml()
        self.name = self.meta_yaml['name']
        self.version = self.meta_yaml['version']
        self.updated = self.meta_yaml['updated']
        self.screenshots = self.meta_yaml['screenshots']
        self.links = self.meta_yaml['links']

    def validate_meta_yaml(self):
        assert 'name' in self.meta_yaml, '%s: meta.yaml missing "name" key' % self.path
        assert 'version' in self.meta_yaml, '%s: meta.yaml missing "version" key' % self.path
        assert 'updated' in self.meta_yaml, '%s: meta.yaml missing "updated" key' % self.path
        assert 'screenshots' in self.meta_yaml, \
            '%s: meta.yaml missing "screenshots" key' % self.path
        assert 'links' in self.meta_yaml, '%s: meta.yaml missing "links" key' % self.path

    def load_summary(self):
        self._load_text(['summary.html', 'summary.htm', 'summary.md'],
                        'summary_html')

    def load_description(self):
        self._load_text(['description.html', 'description.htm', 'description.md'],
                        'description_html')

    def _load_text(self, filepaths, attribute):
        assert any(os.path.isfile(os.path.join(self.path, filepath))
                   for filepath in filepaths)
        for filepath in filepaths:
            fullpath = os.path.join(self.path, filepath)
            if os.path.isfile(fullpath):
                with codecs.open(fullpath,
                                 mode='r',
                                 encoding='utf-8') as f_in:
                    text = f_in.read()
                    break
        if filepath.endswith('.md'):
            setattr(self, attribute, markdown.markdown(text))
        else:
            # Pre-existing HTML is often malformed and full HTML documents. We need to tolerantly
            # parse it (using html5lib) and then only return the contents (the string markup
            # contents of the body tag). We also fix up image sources.
            doc = BeautifulSoup(text, "html5lib")
            for img in doc.find_all('img'):
                if not img.attrs['src'].startswith('../img/'):
                    img.attrs['src'] = '../img/%s' % img.attrs['src'] 
            body = doc.find("body").prettify()
            body = re.sub("^<body>", "", body)
            body = re.sub("</body>$", "", body)
            setattr(self, attribute, body)


def build_categories(loader):
    paths = [os.path.abspath(path)
             for path in glob.glob(os.path.join(DATA_DIR, '*'))
             if os.path.isdir(path)]
    for path in paths:
        build_category(loader, path)


def build_category(loader, path):
    category = Category(path)
    for game in category.games:
        print("build_category working on game: %s" % game)
        for image in game.images:
            print("build_category working on image: %s" % image)
            destination = os.path.join(OUTPUT_DIR, "img", os.path.basename(image))
            assert not os.path.isfile(destination), 'destination %s already exists.' % destination
            shutil.copyfile(image, destination)
    template = loader.get_template('category.html')
    output_text = template.render(date=datetime.date.today().isoformat(),
                                  active_section=category.category_name,
                                  category_title=category.category_title,
                                  games=category.games)
    os.mkdir(os.path.join(OUTPUT_DIR, category.category_name))
    with open(os.path.join(OUTPUT_DIR, category.category_name, 'index.html'), 'w') as f_out:
        f_out.write(output_text)
    for game in category.games:
        build_game(loader, game, category)


def build_game(loader, game, category):
    template = loader.get_template('game_detail.html')
    output_text = template.render(date=datetime.date.today().isoformat(),
                                  active_section=category.category_name,
                                  category_title=category.category_title,
                                  game=game)
    fullpath = os.path.join(OUTPUT_DIR,
                            category.category_name,
                            '%s.html' % game.game_id)
    with codecs.open(fullpath,
                     mode='w',
                     encoding='utf-8') as f_out:
        f_out.write(output_text)


@contextlib.contextmanager
def get_pool():
    pool = multiprocessing.Pool(max(multiprocessing.cpu_count() - 2, 1))
    try:
        yield pool
    finally:
        pool.close()
        pool.join()
        pool.terminate()


def compress_output():
    pngs = []
    texts = []
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for name in files:
            fullpath = os.path.join(root, name)
            if fullpath.endswith('.png'):
                pngs.append(fullpath)
            if re.search('.*\.(html|htm|js|css|map|ttf|svg)$', fullpath):
                texts.append(fullpath)
    with get_pool() as pool:
        pool.map(compress_png, pngs)
        pool.map(gzip_text, texts)


def compress_png(fullpath):
    extension = os.path.splitext(fullpath)[1]
    cache_filename = "%s%s" % (calculate_hash(fullpath), extension)
    cache_fullpath = os.path.join(CACHE_DIR, cache_filename)
    if not os.path.isfile(cache_fullpath):
        shutil.copyfile(fullpath, cache_fullpath)
        subprocess.check_call(['optipng', '-o7', '-clobber', '-strip', 'all', cache_fullpath])
    shutil.copyfile(cache_fullpath, fullpath)


def gzip_text(fullpath):
    subprocess.check_call(['gzip', '--best', '--keep', '--verbose', fullpath])


def generate_manifest():
    paths = []
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for name in files:
            paths.append(os.path.join(root, name))
    with get_pool() as pool:
        result = pool.map(calculate_hash, paths)
    with open(os.path.join(OUTPUT_DIR, 'manifest.txt'), 'w') as f_out:
        for (path, checksum) in zip(paths, result):
            subpath = path.replace(OUTPUT_DIR, '', 1).lstrip(os.path.sep)
            subpath = subpath.replace(ntpath.sep, posixpath.sep)
            f_out.write('"%s" %s\n' % (subpath, checksum))


def calculate_hash(filepath, algorithm=hashlib.md5, length=16 * 1024):
    m = algorithm()
    with open(filepath) as f_in:
        while True:
            buf = f_in.read(length)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def main():
    print('starting...')
    loader = TemplateLoader()
    delete_output_directory()
    if not os.path.isdir(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    copy_static_files()
    os.mkdir(os.path.join(OUTPUT_DIR, "img"))
    build_index(loader)
    build_categories(loader)
    compress_output()
    generate_manifest()
    print('done.')


if __name__ == '__main__':
    main()
