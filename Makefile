TRAVIS_REPO_SLUG ?= fernandoe/fe-pessoa-api
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

test:
	cd src; pytest

ci.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s

pip.freeze:
	pip freeze -r requirements.txt

compose-migrate:
	docker-compose exec api-conta python manage.py migrate
	docker-compose exec api-pessoa python manage.py migrate

requirements:
	docker run --rm '${TRAVIS_REPO_SLUG}:${TAG}' pip freeze -r /requirements.txt
