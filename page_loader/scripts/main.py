#!/usr/bin/env python
import argparse
import os
import sys

from page_loader.loader import download  # noqa


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

    download(args.url, args.output)

    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.exit()
