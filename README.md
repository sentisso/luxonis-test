## Usage
1. just run `docker compose up -d`

Upon starting the services, the `web` container will show an empty page, that's because the `scraper` service probably hasn't finished scraping sreality.cz, give it some time or see the progress via `docker logs luxonis-scraper --follow`.

## Requirements
- [x] use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell)
- [x] save it in a Postgresql database
- [x] implement a simple HTTP server in python and show these 500 items on a simple page (title and image)
- [x] put everything to single docker compose command so that I can just run `docker-compose up` in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

## Possible solutions
### #1
Simply store the JSON contents at https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500 to the Postgres database.

### #2
Well, use https://scrapy.org/ to scrape https://www.sreality.cz/hledani/prodej/byty?strana=<1 to X> until we hit 500