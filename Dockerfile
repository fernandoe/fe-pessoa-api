FROM fernandoe/docker-python:3.7.0-alpine3.8
LABEL maintainer="Fernando Espíndola <fer.esp@gmail.com>"

ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD ./docker/run.sh /run.sh
ADD ./src /app

WORKDIR /app

CMD ["/run.sh"]
