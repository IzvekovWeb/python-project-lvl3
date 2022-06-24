import os
from URLDownloader import URLDownloader


def download(url, output=os.getcwd()):

    downloader = URLDownloader(url, output)
    page_name = downloader.download()

    print(page_name)
