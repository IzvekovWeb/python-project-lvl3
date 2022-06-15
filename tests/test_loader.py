from page_loader.page_loader import loader
import tempfile

def test_loader():

    with tempfile.TemporaryDirectory() as tmpdirname:
        print('TMP: ', tmpdirname)
        loader('https://page-loader.hexlet.repl.co/', tmpdirname)
