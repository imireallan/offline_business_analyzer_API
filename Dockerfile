FROM python:3.7.8-alpine3.12

ENV PYTHONUNBUFFERED 1

RUN apk --update add \
	build-base \
	postgresql \
	postgresql-dev \
	libpq

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

