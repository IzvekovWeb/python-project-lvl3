from page_loader.scripts.main import get_logging_dict_config

def test_get_logging_dict_config():

    with open('tests/fixtures/log_result.txt') as r:
        text = r.read()
    assert str(get_logging_dict_config()) == str(text)
