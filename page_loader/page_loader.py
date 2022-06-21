import os
import requests

from page_loader.create_name import create_file_name


def download(url, output=os.getcwd()):
    file_name = create_file_name(url)
    full_path = os.path.join(output, file_name)

    r = requests.get(url)

    with open(full_path, 'w+') as file:
        file.write(r.text)

    return file_name
