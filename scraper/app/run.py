import logging
import scraper
import repos

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s [%(asctime)s] %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

if __name__ == '__main__':
    repos.wait_and_connect_db()

    estates = scraper.get_flats_scrapy(500)

    if estates is not None:
        repos.insert_estates(estates)
    else:
        logging.error("No estates found")

    repos.cur.close()
    repos.conn.close()
