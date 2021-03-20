import logging
from pymongo import MongoClient

client = None
collection = None

def start(stringConn, db, aCollection):
    global client, collection
    client = MongoClient(stringConn)
    logging.info("Connected to Mongo")
    db = client[db]
    collection = db[aCollection]

def existVideo(videoId):
    global collection
    row = collection.find_one({"id":videoId})
    return row is not None

def insertVideo(video):
    global collection
    collection.insert_one(video)