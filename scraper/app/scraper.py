from _types import TEstate
from typing import List
import requests
import logging
import spiders
import time


def get_flats_json(per_page, retries=5) -> List[TEstate]:
    """
    Fetch flats from sreality API.
    """
    logging.info("Fetching flats in JSON...")

    url = "https://www.sreality.cz/api/cs/v2/estates"
    try:
        r = requests.get(
            url,
            params={
                "per_page": per_page,
                "category_main_cb": 1,
                "category_type_cb": 1
            }
        )
    except Exception as e:
        logging.error(e)
        logging.info(f"Retrying in 5 seconds ({retries} retries left)...")
        time.sleep(5)
        get_flats_json(retries - 1)

    data = r.json()
    estates: List[TEstate] = []
    for estate in data["_embedded"]["estates"]:
        estates.append(
            {
                "hash_id": estate["hash_id"],
                "title": estate["name"],
                "image_url": estate["_links"]["images"][0]["href"]
            }
        )

    return estates


def get_flats_scrapy(limit) -> List[TEstate]:
    """
    Fetch flats using scrapy.
    """
    logging.info("Fetching flats using scrapy...")

    spiders.process.crawl(spiders.EstatesSpider, limit=limit)
    spiders.process.start()

    return spiders.CustomPipeline.items
