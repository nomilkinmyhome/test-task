.PHONY: clean
SHELL := /bin/bash

fmt:
	poetry run black .


start:
	docker-compose up


down:
	docker-compose down


migrations:
	poetry run python manage.py makemigrations


migrate:
	docker exec -ti app poetry run python manage.py migrate