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

def insertCodes(codes):
    global collection
    collection.insert_many(codes)

def listAllCodes():
    global collection
    return collection.find()