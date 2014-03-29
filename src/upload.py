#!/usr/bin/env python

import boto
import contextlib
import cStringIO as StringIO
import datetime
import os
import pprint
import re

# -----------------------------------------------------------------------------
#   Logging.
# -----------------------------------------------------------------------------
import logging
logger = logging.getLogger('upload')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
# -----------------------------------------------------------------------------


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')


def get_manifest_from_file(f_in):
    return_value = {}
    for line in f_in:
        match = re.search('^\"(?P<path>[^"]+)\" (?P<checksum>.*)$', line)
        assert match, 'get_local_manifest() line %s doesn\'t match pattern' % line
        return_value[match.groupdict()['path']] = match.groupdict()['checksum']
    return return_value


def get_local_manifest():
    with open(os.path.join(OUTPUT_DIR, 'manifest.txt')) as f_in:
        return get_manifest_from_file(f_in)


def upload_to_s3(s3_bucket='mindgames.asimihsan.com'):
    modified_files = []
    local_manifest = get_local_manifest()
    with contextlib.closing(boto.connect_s3()) as conn:
        with contextlib.closing(boto.connect_cloudfront()) as conn_cloudfront:
            cloudfront_distribution = [elem for elem in conn_cloudfront.get_all_distributions()
                                       if elem.origin.dns_name.startswith(s3_bucket)][0]
            cloudfront_distribution = cloudfront_distribution.get_distribution()
            bucket = conn.get_bucket(s3_bucket)

            remote_manifest_key = bucket.get_key('manifest.txt')
            if not remote_manifest_key:
                logger.info('remote manifest does not exist')
                remote_manifest = {}
                remote_manifest_key = bucket.new_key('manifest.txt')
            else:
                logger.info('remote manifest exists')
                contents = remote_manifest_key.get_contents_as_string()
                remote_manifest = get_manifest_from_file(StringIO.StringIO(contents))


            for (local_filepath, local_checksum) in local_manifest.items():
                if (local_filepath.endswith('.gz') and
                        re.sub(r'(\.gz)$', '', local_filepath) in local_manifest):
                    logger.info('skipping GZIP\'d local_filepath %s' % local_filepath)
                    continue
                key = bucket.get_key(local_filepath)
                if (key is not None and
                        remote_manifest.get(local_filepath, None) == local_checksum):
                    logger.info('local_filepath %s exists, and identical to '
                                'remote, so skip' % local_filepath)
                    continue
                modified_files.append(local_filepath)
                if key is None:
                    logger.info('local_filepath %s does not exist' % local_filepath)
                    key = bucket.new_key(local_filepath)
                gzipped_filepath = '%s.gz' % local_filepath
                is_gzipped = gzipped_filepath in local_manifest
                if is_gzipped:
                    local_fullpath = os.path.join(OUTPUT_DIR, gzipped_filepath)
                else:
                    local_fullpath = os.path.join(OUTPUT_DIR, local_filepath)
                if is_gzipped:
                    logger.info('local filepath %s is gzipped so change Content-Encoding' %
                                local_filepath)
                    key.set_metadata("Content-Encoding", "gzip")
                if local_filepath.endswith('.html'):
                    logger.info('local_filepath %s is HTML, so set Content-Type header w/ utf-8' %
                                local_filepath)
                    key.set_metadata("Content-Type", "text/html; charset=utf-8")
                maybe_set_expires(key, local_filepath)
                key.set_contents_from_filename(local_fullpath)
                key.make_public()
                logger.info('uploaded local_filepath: %s' % local_filepath)

    modified_files.sort()
    if len(modified_files) > 0:
        logger.info("invalidate the following on cloudfront:\n%s" % pprint.pformat(modified_files))
        conn_cloudfront.create_invalidation_request(cloudfront_distribution.id, modified_files)
    else:
        logger.info("no modified files, so nothing to invalidate on cloudfront")

    logger.info('uploading manifest file...')
    remote_manifest_key.set_contents_from_filename(os.path.join(OUTPUT_DIR, 'manifest.txt'))
    remote_manifest_key.make_public()


def maybe_set_expires(key, local_filepath):
    if not re.search(r'^.*\.(png|gif|jpg|eot|svg|ttf|woff)$', local_filepath):
        logger.info('not setting expires for local_filepath: %s' % local_filepath)
        return
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    expires = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    logger.info("Setting Expires to %s for local_filepath %s" % (expires, local_filepath))
    key.set_metadata("Expires", expires)


def main():
    upload_to_s3()


if __name__ == "__main__":
    main()
