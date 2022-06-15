from page_loader.page_loader import download
import tempfile
# import requests_mock


def test_loader(requests_mock):

    # requests_mock.get('http://test.com', text='data')
    # assert 'data' ==requests.get('http://test.com').text

    with tempfile.TemporaryDirectory() as tmpdirname:

        download('https://page-loader.hexlet.repl.co/', tmpdirname)

        with open('tests/fixtures/loader_result.html') as fixture:
            result = fixture.read()
        
        tmp_file = tmpdirname + '/page-loader-hexlet-repl-co.html'
        try:
            with open(tmp_file) as tmp_result:
                tmp = tmp_result.read()
        except FileNotFoundError:
            print(f'Error: FileNotFoundError ({tmp_file})')
            return

        assert result == tmp

test_loader()