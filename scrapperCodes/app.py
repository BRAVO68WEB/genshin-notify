from dotenv import load_dotenv
import os, time, logging
import schedule

load_dotenv()

MONGO_CONN = os.environ.get("MONGO_CONN")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLL = os.environ.get("MONGO_COLL")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

REPEAT_SCRAP_IN_MINUTES = os.environ.get("REPEAT_SCRAP_IN_MINUTES")

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)

from Mongo import client as MongoClient
from Redis import client as RedisClient

MongoClient.start(MONGO_CONN,MONGO_DB,MONGO_COLL)
RedisClient.start(REDIS_HOST,REDIS_PORT)

from scrapper import scrapper

schedule.every(REPEAT_SCRAP_IN_MINUTES).minutes.do(scrapper)

while True:
    schedule.run_pending()
    time.sleep(1)