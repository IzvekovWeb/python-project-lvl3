import os
from URLDownloader import URLDownloader


def download(url, output=os.getcwd()):
    downloader = URLDownloader(url, output)

    print(downloader.download())

# download('https://page-loader.hexlet.repl.co/',
# 'output')
