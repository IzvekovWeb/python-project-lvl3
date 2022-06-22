import os
import sys
sys.path.append('/mnt/d/Pro100Sany/Python/Hexlet/python-project-lvl3/page_loader') # noqa

from URLDownloader import URLDownloader  # noqa


def download(url, output=os.getcwd()):
    downloader = URLDownloader(url, output)

    print(downloader.download())
