#!/usr/bin/env python
from page_loader.page_loader import loader
import argparse
import os


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

    page = loader(args.url, output=args.output)
    print(page)


if __name__ == '__main__':
    main()
