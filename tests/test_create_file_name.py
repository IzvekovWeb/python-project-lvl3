from URLDownloader import URLDownloader


def test_create_file_name():
    downloader = URLDownloader('https://page-loader.hexlet.repl.co/')

    test_url = "https://page-loader.hexlet.repl.co/"
    assert downloader.create_file_name(test_url) == "page-loader-hexlet-repl-co-.html"

    test_url = "https://example.com/index.html"
    assert downloader.create_file_name(test_url) == "example-com-index.html"

    test_url = "https://page-loader.hexlet.repl.co/assets/professions/nodejs.png"
    assert downloader.create_file_name(test_url, 'png') == "page-loader-hexlet-repl-co-assets-professions-nodejs.png"

    test_url = "https://page-loader.hexlet.repl.co"
    assert downloader.create_file_name(test_url, 'files') == "page-loader-hexlet-repl-co_files"
