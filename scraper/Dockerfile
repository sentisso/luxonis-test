FROM python:3.11.7 AS base
WORKDIR /scraper
RUN pip install --upgrade pip
RUN apt-get install libpq-dev

FROM base AS dependencies
COPY ./requirements.txt /scraper
RUN pip install -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium

FROM dependencies
COPY . /scraper
WORKDIR /scraper/app
CMD ["python", "run.py"]