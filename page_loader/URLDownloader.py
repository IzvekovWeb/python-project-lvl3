import os
import requests
import re

from bs4 import BeautifulSoup


class URLDownloader:
    """Class URLDownloader is used to download web pages by URL"""

    def __init__(self, url, output=os.getcwd()):
        self.url = url
        self.output = output
        host = ''
        self.host = host

    def download(self):
        page_name = self.page_download()
        self.images_download(page_name)
        return page_name

    def page_download(self):
        file_name = self.create_file_name(self.url)
        full_path = os.path.join(self.output, file_name)

        r = requests.get(self.url)

        with open(full_path, 'w+') as file:
            file.write(r.text)

        return file_name

    def images_download(self, index):
        with open(os.path.join(self.output, index), "r") as f:
            contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')

        # Парсим html и записываем все ссылки картинок в список
        images = soup.find_all('img')
        image_links = [
            {'old_p': img['src'][1:]}
            if img['src'].startswith('/')
            else {'old_p': img['src']}
            for img in images
        ]

        # Создаем папку для файлов, если её нет
        folder_name = self.create_file_name(self.url, 'files')
        path_to_folder = os.path.join(self.output, folder_name)
        if not os.path.exists(path_to_folder):
            os.mkdir(path_to_folder)

        # Скачиваем и переименовываем все картинки
        for i in range(len(image_links)):
            img_old_p = image_links[i]['old_p']
            img_full_path = os.path.join(self.url, img_old_p)
            ext = img_old_p[img_old_p.rfind(".") + 1:]

            new_img_name = self.create_file_name(img_full_path, ext)

            r = requests.get(img_full_path)

            img_new_p = os.path.join(folder_name, new_img_name)
            with open(os.path.join(self.output, img_new_p), "wb") as fi:
                fi.write(r.content)

            image_links[i]['new_p'] = img_new_p

        # Заменяем ссылки в HTML
        new_soup = BeautifulSoup(contents, 'html.parser')
        for link in image_links:
            new_soup.img['src'] = (link['new_p'])

        with open(os.path.join(self.output, index), "w") as f:
            f.write(new_soup.prettify())

    def files_download(self):
        pass

    def create_file_name(self, url, ext='html'):

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

# downloader = URLDownloader('https://page-loader.hexlet.repl.co/', 'output')
# page_name = downloader.page_download()
