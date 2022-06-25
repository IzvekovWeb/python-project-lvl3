import os
import requests
import re
import logging
import sys

from progress.bar import Bar
from urllib import parse as urllib
from bs4 import BeautifulSoup

from requests.exceptions import ConnectionError

logger = logging.getLogger("app.URLDownloader")


class URLDownloader:
    """Class URLDownloader is used to download web pages by URL"""

    def __init__(self, url, output=os.getcwd()):
        logger.debug('Initializing URLDownloader object')
        self.url = url
        self.output = output
        self.host = urllib.urlparse(url).netloc

    def download(self):
        logger.debug('Start downloading web page')
        page_name = self.page_download()
        self.images_download(page_name)
        self.css_download(page_name)
        self.js_download(page_name)
        return page_name

    def page_download(self):
        file_name = self._create_file_name(self.url)
        full_path = os.path.join(self.output, file_name)

        try:
            r = requests.get(self.url)
        except ConnectionError:
            logger.critical("Requests: ConnectionError")
            sys.exit(50)

        try:
            with open(full_path, 'w+') as file:
                file.write(r.text)
            logger.info(f'File {file_name} has been downloaded')
        except OSError as e:
            logger.error(f'Write file error: {e}')
            sys.exit(40)

        return file_name

    def images_download(self, index):
        logger.debug('Images downloading')
        # Получаем ссылки из тегов
        image_links = self._parce_html(index, 'img')

        # Создаём папку
        folder_name = self._create_folder()

        # Скачиваем файлы
        self._download_files(
            image_links,
            folder_name,
            type='img'
        )

        # Заменяем ссылки в HTML
        self._rewrite_links_html(index, image_links, type='img')

    def css_download(self, index):
        logger.debug('CSS downloading')
        css_links = self._parce_html(index, type='css')

        folder_name = self._create_folder()

        # Скачиваем файлы
        self._download_files(
            css_links,
            folder_name,
            type='css'
        )

        # Заменяем ссылки в HTML
        self._rewrite_links_html(index, css_links, type='css')

    def js_download(self, index):
        logger.debug('JS downloading')
        js_links = self._parce_html(index, type='js')

        folder_name = self._create_folder()

        # Скачиваем файлы
        self._download_files(
            js_links,
            folder_name,
            type='js'
        )

        # Заменяем ссылки в HTML
        self._rewrite_links_html(index, js_links, type='js')

    def _create_file_name(self, url, ext='html'):

        # Отделяем схему (https://)
        file_name = re.search(r"(?<=^https:\/\/).+", url, flags=re.MULTILINE)
        # (?<=https:\/\/(?!.*https:\/\/)).+

        # Заменяем разделители на дефис
        file_name = re.sub(r'[./;,\s_:]', '-', file_name.group(0))

        def add_extension(name, ext):
            # Проверяем наличие расширения
            if re.search(fr'([\._\-])({re.escape(ext)})+$', name):
                # Форматируем расширение точкой
                name = re.sub(fr'([\._\-])({re.escape(ext)})+$', r'.\2', name)
            else:
                # Или добавляем расширение
                if ext != 'files':
                    name += f'.{ext}'
                else:
                    name += '_files'
            return name

        file_name = add_extension(file_name, ext)

        return file_name

    def _parce_html(self, index, type):  # noqa: C901
        """Types: img | js | css

        returns: list [{'old_p': <old_path>}]
        """
        try:
            with open(os.path.join(self.output, index), "r") as f:
                contents = f.read()
            logger.debug('Request is done')
        except OSError as e:
            logger.critical(f'File read Error: {e}')
            sys.exit(50)

        # Парсим html и записываем все ссылки картинок в список
        soup = BeautifulSoup(contents, 'html.parser')

        if type == 'img':
            tags = soup.find_all('img')
            links = [
                {'old_p': tag['src'][1:]}
                if tag['src'].startswith('/')
                else {'old_p': tag['src']}
                for tag in tags
            ]
            logger.info('IMG links successfully parsed')
        elif type == 'css':
            tags = soup.find_all('link')
            links = []
            for tag in tags:
                if tag['rel'][0] == 'stylesheet':
                    if tag['href'].startswith('/'):
                        links.append({'old_p': tag['href'][1:]})
                    else:
                        links.append({'old_p': tag['href']})
            logger.info('CSS links successfully parsed')
        elif type == 'js':
            tags = soup.find_all('script')
            links = []
            for tag in tags:
                if tag.has_attr('src'):
                    if tag['src'].startswith('/'):
                        links.append({'old_p': tag['src'][1:]})
                    else:
                        links.append({'old_p': tag['src']})
            logger.info('JS links successfully parsed')

        return links

    def _create_folder(self):

        # Создаем папку для файлов, если её нет
        folder_name = self._create_file_name(self.url, 'files')
        path_to_folder = os.path.join(self.output, folder_name)

        if not os.path.exists(path_to_folder):
            try:
                os.mkdir(path_to_folder)
                logger.info(f'Folder {folder_name} created')
            except Exception as e:
                logger.critical(f'Directory create error: {e}')
                raise IsADirectoryError("Folder isn't created")

        return folder_name

    def _download_files(self, links, folder_name, type):  # noqa: C901

        bar = Bar(f'Downloading {type}', max=len(links))

        for i in range(len(links)):

            # Old path, name
            old_path = links[i]['old_p']
            full_old_path = os.path.join(self.url, old_path)

            ext = old_path[old_path.rfind(".") + 1:]

            # New path, name
            new_name = self._create_file_name(full_old_path, ext)
            new_path = os.path.join(folder_name, new_name)

            try:
                r = requests.get(full_old_path)
                logger.debug('Request is done')
            except ConnectionError:
                logger.critical('ConnectionError')
                sys.exit(50)

            if type == 'img':
                try:
                    with open(os.path.join(self.output, new_path), 'wb') as f:
                        f.write(r.content)
                    logger.info('Image seccsesfully downloaded')
                except OSError as e:
                    logger.error(f'File write Error: {e}')
            else:
                try:
                    with open(os.path.join(self.output, new_path), 'w') as f:
                        f.write(r.text)
                    logger.info(f'{type} file seccsesfully downloaded')
                except OSError as e:
                    logger.error(f'File write Error: {e}')

            links[i]['new_p'] = new_path
            bar.next()
        bar.finish()

    def _rewrite_links_html(self, html, links, type): # noqa
        try:
            with open(os.path.join(self.output, html), "r") as f:
                contents = f.read()
            logger.debug('Request is done')
        except OSError as e:
            logger.critical(f'File read Error: {e}')
            sys.exit(50)

        # Заменяем ссылки в HTML
        new_soup = BeautifulSoup(contents, 'html.parser')
        if type == 'img':
            for link in links:
                new_soup.img['src'] = (link['new_p'])
        elif type == 'css':
            for link in links:
                new_soup.link['href'] = (link['new_p'])
        elif type == 'js':
            for link in links:
                new_soup.script['src'] = (link['new_p'])
        try:
            with open(os.path.join(self.output, html), "w") as f:
                f.write(new_soup.prettify())
            logger.info('Links rewrited')
        except OSError as e:
            logger.error(f'File write Error: {e}')
            sys.exit(40)
