.PHONY: help install migrate run test

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make migrate    - Run Django migrations"
	@echo "  make run        - Run the Django development server"
	@echo "  make test       - Run tests"
	@echo "  make shell      - Open Django shell"

install:
	pip install -r requirements.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

test:
	python manage.py test

shell:
	python manage.py shell
