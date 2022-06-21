from page_loader.page_loader import create_file_name


def test_create_file_name():

    test_url = "https://page-loader.hexlet.repl.co/"
    assert create_file_name(test_url) == "page-loader-hexlet-repl-co-.html"

    test_url = "https://example.com/index.html"
    assert create_file_name(test_url) == "example-com-index.html"

    test_url = "https://page-loader.hexlet.repl.co/assets/professions/nodejs.png"
    assert create_file_name(test_url, 'png') == "page-loader-hexlet-repl-co-assets-professions-nodejs.png"

    test_url = "https://page-loader.hexlet.repl.co"
    assert create_file_name(test_url, 'files') == "page-loader-hexlet-repl-co_files"
