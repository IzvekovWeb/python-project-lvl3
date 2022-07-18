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
        '-o',
        '--output',
        default=os.getcwd(),
        help='set path to save')

    args = parser.parse_args()

    try:
        download(args.url, args.output)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.exit(1)
