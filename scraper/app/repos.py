from psycopg2 import extensions, extras
from _types import TEstate
from typing import List
import psycopg2
import logging
import socket
import time
import os

conn: psycopg2.extensions.connection = None
cur: psycopg2.extensions.cursor = None


def wait_and_connect_db():
    """
    Wait for database to be ready and connect to it.
    """
    global conn, cur
    port = 5432
    host = "db"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host, port))
            s.close()
            break
        except socket.error as ex:
            time.sleep(1)

    conn = psycopg2.connect(
        host="db",
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def insert_estates(estates: List[TEstate]):
    """
    Insert estates into database.
    """
    global conn, cur

    for estate in estates:
        logging.info(f"Inserting estate {estate['hash_id']}...")
        cur.execute(
            "INSERT INTO sreality_estates (hash_id, title, image_url) VALUES (%s, %s, %s)"
            "ON CONFLICT (hash_id) DO NOTHING",
            (estate["hash_id"], estate["title"], estate["image_url"])
        )

    conn.commit()
    logging.info(f"Inserted {len(estates)} estates")