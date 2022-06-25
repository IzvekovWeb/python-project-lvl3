# Установка зависимостей проекта
install:
	poetry install

# Запуск программ
page-loader:
	poetry run page-loader --output output 'https://page-loader.hexlet.repl.co/'
# poetry run page-loader --output output 'https://ru.hexlet.io/courses'
	

# Сборка проекта в whl файл
build:
	poetry build

# Установка wheel файла
package-install:
	python3 -m pip install --force-reinstall dist/*.whl

# Проверка на lint
lint:
	poetry run flake8 page_downloader

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_downloader 

test-coverage-xml:
	poetry run pytest --cov=page_downloader --cov-report xml

.PHONY: install test lint selfcheck check build page-loader