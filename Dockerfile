FROM python:3.7.8-alpine3.12

ENV PYTHONUNBUFFERED 1

RUN apk add --update bash \
 build-base \
 postgresql \
 postgresql-dev \
 libpq

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt
