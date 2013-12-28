#!/usr/bin/env python

import codecs
import glob
import jinja2
import markdown
import operator
import os
import shutil
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'template')


def delete_output_directory():
    shutil.rmtree(OUTPUT_DIR)


def copy_static_files():
    for source_dir in ['css']:
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
    output_text = template.render(active_section="index")
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
    required_files = ['description.md', 'meta.yaml', 'summary.md']

    def __init__(self, path):
        self.path = path
        self.game_id = os.path.basename(path)
        for filename in self.required_files:
            fullpath = os.path.join(self.path, filename)
            assert os.path.isfile(fullpath), 'could not find file %s' % fullpath
        self.load_meta_yaml()
        self.load_summary()
        self.load_description()
        self.images = [filepath for filepath in glob.glob(os.path.join(self.path, '*'))
                       if any(filepath.endswith(ext) for ext in ['.jpg', '.gif', '.png'])]

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
        with codecs.open(os.path.join(self.path, 'summary.md'),
                         mode='r',
                         encoding='utf-8') as f_in:
            text = f_in.read()
        self.summary_html = markdown.markdown(text)

    def load_description(self):
        with codecs.open(os.path.join(self.path, 'description.md'),
                         mode='r',
                         encoding='utf-8') as f_in:
            text = f_in.read()
        self.description_html = markdown.markdown(text)


def build_categories(loader):
    paths = [os.path.abspath(path)
             for path in glob.glob(os.path.join(DATA_DIR, '*'))
             if os.path.isdir(path)]
    for path in paths:
        build_category(loader, path)


def build_category(loader, path):
    category = Category(path)
    for game in category.games:
        for image in game.images:
            destination = os.path.join(OUTPUT_DIR, "img", os.path.basename(image))
            assert not os.path.isfile(destination), 'destination %s already exists.' % destination
            shutil.copyfile(image, destination)
    template = loader.get_template('category.html')
    output_text = template.render(active_section=category.category_name,
                                  category_title=category.category_title,
                                  games=category.games)
    os.mkdir(os.path.join(OUTPUT_DIR, category.category_name))
    with open(os.path.join(OUTPUT_DIR, category.category_name, 'index.html'), 'w') as f_out:
        f_out.write(output_text)
    for game in category.games:
        build_game(loader, game, category)


def build_game(loader, game, category):
    template = loader.get_template('game_detail.html')
    output_text = template.render(active_section=category.category_name,
                                  category_title=category.category_title,
                                  game=game)
    with open(os.path.join(OUTPUT_DIR,
                           category.category_name,
                           '%s.html' % game.game_id), 'w') as f_out:
        f_out.write(output_text)


def main():
    loader = TemplateLoader()
    delete_output_directory()
    copy_static_files()
    os.mkdir(os.path.join(OUTPUT_DIR, "img"))
    build_index(loader)
    build_categories(loader)


if __name__ == '__main__':
    main()
