from dotenv import load_dotenv
import os, logging

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_TOKEN")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

MONGO_CONN = os.environ.get("MONGO_CONN")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLL = os.environ.get("MONGO_COLL")

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)

from Telegram import client as TelegramClient
from Redis import client as RedisClient
from Mongo import client as MongoClient

TelegramClient.start(TOKEN)
MongoClient.start(MONGO_CONN,MONGO_DB,MONGO_COLL)
RedisClient.start(REDIS_HOST,REDIS_PORT)


