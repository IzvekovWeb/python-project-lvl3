import requests
import os

from bs4 import BeautifulSoup

from page_loader.create_name import create_file_name


def download_images(url, output, index):
    with open(os.path.join(output, index), "r") as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    images = soup.find_all('img')
    image_links = [
        img['src'][1:] if img['src'].startswith('/') else img['src']
        for img in images
    ]

    # Создаем папку для файлов, если её нет
    folder_name = create_file_name(url, 'files')
    path_to_dir = os.path.join(output, folder_name)
    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)

    # Скачиваем и переименовываем все картинки
    for img in image_links:
        img_full_path = os.path.join(url, img)
        ext = img[img.rfind(".") + 1:]

        new_img_name = create_file_name(img_full_path, ext)

        r = requests.get(img_full_path)
        print(r.content)

        path = os.path.join(path_to_dir, new_img_name)
        with open(path, "wb") as fi:
            fi.write(r.content)
