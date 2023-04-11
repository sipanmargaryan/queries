all:
	docker-compose build

run:
	docker-compose up junehome

user:
	docker-compose run --rm junehome python3 manage.py createsuperuser --email=test@gmail.com

migrations:
	docker-compose run --rm junehome python3 manage.py makemigrations

migrate:
	docker-compose run --rm junehome python3 manage.py migrate

shell-in:
	docker-compose run --rm junehome /bin/bash

shell:
	docker-compose run --rm junehome python3 manage.py shell

django-shell:
	docker-compose run --rm junehome python3 manage.py shell

collectstatic:
	docker-compose run --rm junehome python3 manage.py collectstatic --no-input

flush-data:
	docker-compose run --rm junehome python3 manage.py flush --no-input

flake8:
	docker-compose run --rm junehome flake8 .

reset-db:
	docker-compose down
	docker volume rm junehome_postgres_data
	docker-compose up -d postgres
	make migrate
	make load-data
