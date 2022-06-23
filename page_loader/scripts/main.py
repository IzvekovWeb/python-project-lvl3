#!/usr/bin/env python
import argparse
import os

from page_loader.URLDownloader import URLDownloader  # noqa


def main():
    """This programm safe url page on disk"""

    parser = argparse.ArgumentParser(description='Safe URL Page')
    parser.add_argument('url')

    parser.add_argument(
        '-0',
        '--output',
        default=os.getcwd(),
        help='set path to save')

    args = parser.parse_args()

    downloader = URLDownloader(args.url, args.output)

    page_name = downloader.page_download()

    downloader.images_download(page_name)
    downloader.css_download(page_name)
    downloader.js_download(page_name)

    print(page_name)


if __name__ == '__main__':
    main()
