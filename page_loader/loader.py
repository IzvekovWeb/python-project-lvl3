import os
import logging
import logging.config
# import json

from page_loader.URLDownloader import URLDownloader


def download(url, output=os.getcwd()):

    logger.debug('Start program page_loader')

    downloader = URLDownloader(url, output)
    page_name = downloader.download()

    print(page_name)

    logger.debug('Stop programm')

    return page_name


LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s :: %(name)s:%(lineno)s - %(levelname)s - %(message)s"  # noqa: E501
        }
    },
    "handlers": {
        "std": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "detailed"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "detailed",
            "filename": "logs/loader.log"
        },
        "file_info": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "detailed",
            "filename": "logs/file_info.log"
        }
    },
    "loggers": {
        "app": {
            "handlers": ["std", "file", "file_info"],
            "level": "DEBUG"
        }
    }
}


def get_logging_dict_config():  # noqa: C901

    # with open('logs/conf.json') as conf:
    #     log_config = conf.read()
    if not os.path.exists('logs/loader.log'):
        try:
            os.makedirs('logs', exist_ok=True)
            with open('logs/loader.log', 'w'):
                pass
        except Exception:
            raise IsADirectoryError("Path isn't wrong")
    if not os.path.exists('logs/file_info.log'):
        try:
            os.makedirs('logs', exist_ok=True)
            with open('logs/loader.log', 'w'):
                pass
        except Exception:
            raise IsADirectoryError("Path isn't wrong")
    return LOG_CONFIG


logging.config.dictConfig(get_logging_dict_config())
logger = logging.getLogger('app')

logging.getLogger('urllib3').setLevel('CRITICAL')
