import re


def create_file_name(url, ext='html'):

    # Отделяем схему (https://)
    file_name = re.search(r"(?<=^https:\/\/).+", url, flags=re.MULTILINE)
    # (?<=https:\/\/(?!.*https:\/\/)).+

    # Заменяем разделители на дефис
    file_name = re.sub(r'[./;,\s_]', '-', file_name.group(0))

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
