TRAVIS_REPO_SLUG ?= fernandoe/fe-pessoa-server
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

test:
	cd src; pytest

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s

pip.freeze:
	pip freeze -r requirements.txt
