import os
import re


def loader(url, output=os.getcwd()):
    path = "/mnt/d/Pro100Sany/Python/Hexlet/python-project-lvl3/output"
    # output = os.path.join(path)


def create_file_name(url):

    # Отделяе схему (https://)
    file_name = re.search(r"(?<=^https:\/\/).+", url, flags=re.MULTILINE)
    # Заменяем разделители на дефис
    file_name = re.sub(r'[./;,\s_]', '-', file_name.group(0))

    # Проверяем наличие резширения
    if re.search(r'([\._\-])(html)+$', file_name):
        # Форматируем расширение точкой
        file_name = re.sub(r'([\._\-])(html)+$', r'.\2', file_name)
    else:
        # Или добавляем расширение
        file_name += '.html'

    return file_name
