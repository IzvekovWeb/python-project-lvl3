import os
import re
import requests


def download(url, output=os.getcwd()):
    file_name = create_file_name(url)
    output = os.path.join(output, file_name)

    r = requests.get(url)

    with open(output, 'w+') as file:
        file.write(r.text)

    return file_name


def create_file_name(url):

    # Отделяем схему (https://)
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

# download('https://page-loader.hexlet.repl.co/')
