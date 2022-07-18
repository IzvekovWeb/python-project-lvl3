import json
import os
import logging
import logging.config
import sys

from page_loader.URLDownloader import URLDownloader


def download(url, output=os.getcwd()):

    logger.debug('Start program page_loader')

    try:
        downloader = URLDownloader(url, output)
        page_name = downloader.download()
    except Exception:
        sys.exit(1)

    logger.debug('Stop programm')

    print(page_name)

    return os.path.join(output, page_name)


def get_logging_dict_config():

    try:
        with open('logs/conf.json') as conf:
            log_config = json.loads(conf.read())
    except OSError:
        raise

    if not os.path.exists('logs/loader.log') or \
            not os.path.exists('logs/file_info.log'):
        try:
            os.makedirs('logs', exist_ok=True)
            open('logs/loader.log', 'w').close()
            open('logs/file_info.log', 'w').close()
        except Exception:
            raise IsADirectoryError("Path is wrong")

    return log_config


logging.config.dictConfig(get_logging_dict_config())
logger = logging.getLogger('app')

logging.getLogger('urllib3').setLevel('CRITICAL')
