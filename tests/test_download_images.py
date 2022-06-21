from page_loader.image_loader import download_images
from page_loader.page_loader import download

import tempfile
import requests_mock
import os
import shutil



def test_download_images(requests_mock):
    
    with open('tests/fixtures/image_result.png', 'rb') as fixture:
        result = fixture.read()
    result = str(result)
    requests_mock.get('https://page-loader.hexlet.repl.co/assets/professions/nodejs.png', text=result)
    
    with tempfile.TemporaryDirectory() as temp_dir:

        tmp_file = os.path.join(temp_dir, 'page-loader-hexlet-repl-co-_files',\
                                'page-loader-hexlet-repl-co-assets-professions-nodejs.png')

        shutil.copyfile('output/page-loader-hexlet-repl-co-.html', os.path.join(temp_dir, 'page-loader-hexlet-repl-co-.html'))

        download_images('https://page-loader.hexlet.repl.co/', temp_dir, 'page-loader-hexlet-repl-co-.html')

        with open(tmp_file, 'r') as tmp:
            tmp_result = tmp.read()

    tmp_result = str(tmp_result)
    
    assert result == tmp_result
