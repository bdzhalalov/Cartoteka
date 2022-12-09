FROM python:3.10.5-alpine3.15

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install "poetry==1.2"

RUN mkdir -p /var/app/
WORKDIR /var/app/

COPY poetry.lock pyproject.toml /var/app/

RUN apk update \
    && apk add --no-cache curl mariadb-connector-c-dev && apk add --no-cache --virtual python3-dev \
    gcc musl-dev

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

EXPOSE 8000