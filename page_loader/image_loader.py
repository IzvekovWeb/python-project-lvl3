import requests
import os

from bs4 import BeautifulSoup

from page_loader.create_name import create_file_name


def download_images(url, output, index):
    with open(os.path.join(output, index), "r") as f:
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
    folder_name = create_file_name(url, 'files')
    path_to_dir = os.path.join(output, folder_name)
    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)

    # Скачиваем и переименовываем все картинки
    for i in range(len(image_links)):
        img_old_p = image_links[i]['old_p']
        img_full_path = os.path.join(url, img_old_p)
        ext = img_old_p[img_old_p.rfind(".") + 1:]

        new_img_name = create_file_name(img_full_path, ext)

        r = requests.get(img_full_path)

        img_new_p = os.path.join(path_to_dir, new_img_name)
        with open(img_new_p, "wb") as fi:
            fi.write(r.content)

        image_links[i]['new_p'] = img_new_p

    # Заменяем ссылки в HTML
    new_soup = BeautifulSoup(contents, 'html.parser')
    for link in image_links:
        new_soup.img['src'] = (link['new_p'])

    with open(os.path.join(output, index), "w") as f:
        f.write(new_soup.prettify())

# download_images('https://page-loader.hexlet.repl.co/',
# 'output/', 'page-loader-hexlet-repl-co-.html')
