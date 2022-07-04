import tempfile
import os

from page_loader.loader import download  # noqa
from page_loader.URLDownloader import URLDownloader


def test_create_file_name():
    downloader = URLDownloader('https://page-loader.hexlet.repl.co/')

    test_url = "https://page-loader.hexlet.repl.co/"
    assert downloader._create_file_name(test_url) == "page-loader-hexlet-repl-co-.html"

    test_url = "https://example.com/index.html"
    assert downloader._create_file_name(test_url) == "example-com-index.html"

    test_url = "https://page-loader.hexlet.repl.co/assets/professions/nodejs.png"
    assert downloader._create_file_name(test_url, 'png') == "page-loader-hexlet-repl-co-assets-professions-nodejs.png"

    test_url = "https://page-loader.hexlet.repl.co"
    assert downloader._create_file_name(test_url, 'files') == "page-loader-hexlet-repl-co_files"

def test_result_path():
    with tempfile.TemporaryDirectory() as tmpdirname:
        output_file_path = download('https://page-loader.hexlet.repl.co/', tmpdirname)

    assert output_file_path == os.path.join(tmpdirname, 'page-loader-hexlet-repl-co-.html')