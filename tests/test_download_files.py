import tempfile
import requests_mock
import os
import shutil

from page_loader.URLDownloader import URLDownloader


def test_download_images(requests_mock):
    
    with open('tests/fixtures/image_result.png', 'rb') as fixture:
        result = fixture.read()
    result = str(result)

    requests_mock.get('https://page-loader.hexlet.repl.co/assets/professions/nodejs.png', text=result)
    
    
    
    with tempfile.TemporaryDirectory() as temp_dir:

        tmp_file = os.path.join(temp_dir, 'page-loader-hexlet-repl-co-_files',\
                                'page-loader-hexlet-repl-co-assets-professions-nodejs.png')

        shutil.copyfile('tests/fixtures/loader_result.html', os.path.join(temp_dir, 'page-loader-hexlet-repl-co-.html'))

        downloader = URLDownloader('https://page-loader.hexlet.repl.co/', temp_dir)
        downloader.images_download('page-loader-hexlet-repl-co-.html')

        with open(tmp_file, 'r') as tmp:
            tmp_result = tmp.read()

    tmp_result = str(tmp_result)
    
    assert result == tmp_result


def test_download_css(requests_mock):

    with open('tests/fixtures/css_result.css', 'r') as fixture:
        result = fixture.read()
    result = str(result)

    requests_mock.get('https://page-loader.hexlet.repl.co/assets/application.css', text=result)
    
    with tempfile.TemporaryDirectory() as temp_dir:

        tmp_file = os.path.join(temp_dir, 'page-loader-hexlet-repl-co-_files',\
                                'page-loader-hexlet-repl-co-assets-application.css')

        shutil.copyfile('tests/fixtures/loader_result.html', os.path.join(temp_dir, 'page-loader-hexlet-repl-co-.html'))

        downloader = URLDownloader('https://page-loader.hexlet.repl.co/', temp_dir)
        downloader.css_download('page-loader-hexlet-repl-co-.html')

        with open(tmp_file, 'r') as tmp:
            tmp_result = tmp.read()

    tmp_result = str(tmp_result)
    
    assert result == tmp_result


def test_download_js(requests_mock):

    with open('tests/fixtures/js_result.js', 'rb') as fixture:
        result = fixture.read()
    result = str(result)

    requests_mock.get('https://page-loader.hexlet.repl.co/script.js', text=result)
    
    with tempfile.TemporaryDirectory() as temp_dir:

        tmp_file = os.path.join(temp_dir, 'page-loader-hexlet-repl-co-_files',\
                                'page-loader-hexlet-repl-co-script.js')

        shutil.copyfile('tests/fixtures/loader_result.html', os.path.join(temp_dir, 'page-loader-hexlet-repl-co-.html'))

        downloader = URLDownloader('https://page-loader.hexlet.repl.co/', temp_dir)
        downloader.js_download('page-loader-hexlet-repl-co-.html')

        with open(tmp_file, 'r') as tmp:
            tmp_result = tmp.read()

    tmp_result = str(tmp_result)
    
    assert result == tmp_result
