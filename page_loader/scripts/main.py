#!/usr/bin/env python
import argparse
import os
import logging
import logging.config
import json
import sys

from progress.bar import Bar
from URLDownloader import URLDownloader  # noqa


def main():
    """This programm safe url page on disk"""

    logger.debug('Start program page_loader')

    parser = argparse.ArgumentParser(description='Safe URL Page')
    parser.add_argument('url')

    parser.add_argument(
        '-0',
        '--output',
        default=os.getcwd(),
        help='set path to save')

    args = parser.parse_args()
    bar = Bar('Processing', max=5)

    downloader = URLDownloader(args.url, args.output)
    bar.next()
    page_name = downloader.page_download()
    bar.next()
    downloader.images_download(page_name)
    bar.next()
    downloader.css_download(page_name)
    bar.next()
    downloader.js_download(page_name)
    bar.next()
    bar.finish()
    print(page_name)

    logger.debug('Stop programm')
    sys.exit()


def get_logging_dict_config():
    with open('logs/conf.json') as conf:
        log_config = conf.read()
    return json.loads(log_config)


logging.config.dictConfig(get_logging_dict_config())
logger = logging.getLogger('app')

logging.getLogger('urllib3').setLevel('CRITICAL')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.exit()
