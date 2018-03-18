FROM python:3.6.4-alpine

RUN apk add --no-cache build-base mariadb-client-libs

RUN apk add --no-cache --virtual .build-deps mariadb-dev

ADD ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN apk del .build-deps

ADD ./docker/run.sh /run.sh
ADD ./src /app

WORKDIR /app

CMD ["/run.sh"]

# Use this to build MySQL-Client
# https://github.com/gliderlabs/docker-alpine/issues/181





#FROM fernandoe/docker-python:0.0.4
#MAINTAINER Fernando Espíndola <fer.esp@gmail.com>
#
#RUN apt-get update && apt-get install -y \
#  mongodb-clients \
#  mysql-client \
#  python3-pip
#
#RUN apt-get -y autoremove
#RUN apt-get -y autoclean
#RUN apt-get -y clean
#
#ADD ./requirements /requirements
#ADD ./source /app
#
#RUN pip3 install -r /requirements/docker.txt
#
#CMD python3 manage.py runserver 0.0.0.0:8000
#
#WORKDIR /app
