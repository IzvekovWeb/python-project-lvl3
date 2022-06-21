#!/usr/bin/env python
import argparse
import os

from page_loader.page_loader import download
from page_loader.image_loader import download_images


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

    page_name = download(args.url, output=args.output)

    download_images(args.url, args.output, page_name)

    print(page_name)


if __name__ == '__main__':
    main()
