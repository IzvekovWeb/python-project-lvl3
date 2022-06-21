# Установка зависимостей проекта
install:
	poetry install

# Запуск программ
page-loader:
	poetry run page-loader --output output 'https://page-loader.hexlet.repl.co/'

# Сборка проекта в whl файл
build:
	poetry build

# Установка wheel файла
package-install:
	python3 -m pip install --force-reinstall dist/*.whl

# Проверка на lint
lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader 

test-coverage-xml:
	poetry run pytest --cov=page_loader --cov-report xml

.PHONY: install test lint selfcheck check build page-loader