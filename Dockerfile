FROM python:3.6-alpine3.7
COPY . /code
WORKDIR /code
ENV FLASK_CONFIG config.py
RUN apk --no-cache add mariadb-dev build-base bash musl-dev linux-headers
RUN pip install -r md5_light/requirements.txt
