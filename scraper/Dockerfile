FROM python:3.11.7 AS base
WORKDIR /scraper
RUN pip install --upgrade pip
RUN apt-get install libpq-dev
RUN pip install scrapy==2.11.0 scrapy-playwright==0.0.33
RUN playwright install-deps
RUN playwright install chromium

FROM base AS dependencies
COPY ./requirements.txt /scraper
RUN pip install -r requirements.txt

FROM dependencies
COPY . /scraper
WORKDIR /scraper/app
CMD ["python", "run.py"]