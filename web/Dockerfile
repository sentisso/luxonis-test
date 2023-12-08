FROM python:3.11.7-alpine AS base
WORKDIR /web
RUN pip install --upgrade pip
RUN apk add build-base libpq-dev

FROM base AS dependencies
COPY ./requirements.txt /web
RUN pip install -r requirements.txt

FROM dependencies
COPY . /web
WORKDIR /web/app
ENV FLASK_APP=app
CMD ["python", "app.py"]