docker-build:
	docker build -t fernandoe/fe-pessoa-server:local .

docker-bash:
	docker run -it --rm fernandoe/fe-pessoa-server:local /bin/sh

compose-build:
	docker-compose build web

compose-up:
	docker-compose up

compose-migrate:
	docker-compose run --rm web python manage.py migrate

compose-createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser
