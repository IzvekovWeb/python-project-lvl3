import os
import logging
import logging.config
import json

from page_loader.URLDownloader import URLDownloader


def download(url, output=os.getcwd()):

    logger.debug('Start program page_loader')

    downloader = URLDownloader(url, output)
    page_name = downloader.download()

    print(page_name)

    logger.debug('Stop programm')

    return page_name


def get_logging_dict_config():
    with open('logs/conf.json') as conf:
        log_config = conf.read()
    return json.loads(log_config)


logging.config.dictConfig(get_logging_dict_config())
logger = logging.getLogger('app')

logging.getLogger('urllib3').setLevel('CRITICAL')
