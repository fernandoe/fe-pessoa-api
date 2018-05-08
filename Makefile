docker-build:
	docker build -t fernandoe/fe-pessoa-server:local .

test:
	cd src; pytest

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s

pip.freeze:
	pip freeze -r requirements.txt
