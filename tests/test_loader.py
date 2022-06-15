from page_loader.page_loader import loader
import tempfile

def test_loader():

    with tempfile.TemporaryDirectory() as tmpdirname:

        loader('https://page-loader.hexlet.repl.co/', tmpdirname)

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