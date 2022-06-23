import tempfile
import requests_mock
import os

from page_loader.URLDownloader import URLDownloader
from page_loader.page_loader import download


def test_page_download(requests_mock):
    with open('tests/fixtures/loader_result.html') as fixture:
        result = fixture.read()

    requests_mock.get('https://page-loader.hexlet.repl.co/', text=result)

    with tempfile.TemporaryDirectory() as temp_dir:

        downloader = URLDownloader('https://page-loader.hexlet.repl.co/')
        tmp_file = os.path.join(temp_dir, 'page-loader-hexlet-repl-co-.html')

        downloader = URLDownloader('https://page-loader.hexlet.repl.co/', temp_dir)
        downloader.page_download()

        with open(tmp_file) as tmp:
            tmp_result = tmp.read()

    assert result == tmp_result