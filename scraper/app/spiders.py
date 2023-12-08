from scrapy.crawler import CrawlerProcess
import json
import scrapy

process = CrawlerProcess()


class CustomPipeline:
    items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item


class EstatesSpider(scrapy.Spider):
    limit = 10
    name = "sreality_estates"
    start_urls = [
        "https://www.sreality.cz/hledani/prodej/byty",
    ]
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "PLAYWRIGHT_ABORT_REQUEST": lambda request: (
                request.resource_type == "image"
                or ".jpg" in request.url
        ),
        "ITEM_PIPELINES": {
            "spiders.CustomPipeline": 1,
        },
    }

    def __init__(self, limit):
        self.limit = limit

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], meta={"playwright": True})

    def parse(self, response):
        for estate in response.css(".dir-property-list .property"):
            dot_data = json.loads(estate.css("::attr(data-dot-data)").extract()[0])
            yield {
                "hash_id": dot_data["id"],
                "title": estate.css("a.title .name::text").get(),
                "image_url": estate.css("preact div div a:nth-child(1) img::attr(src)").get()
            }

            if len(CustomPipeline.items) >= self.limit:
                print(f"Reached limit {self.limit}")
                return

        next_page = response.css('.paging-full .paging-item:last-child a::attr("href")').get()
        if next_page is not None:
            yield scrapy.Request("https://sreality.cz" + next_page, meta={"playwright": True})
