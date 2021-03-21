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

def existCode(id):
    global collection
    row = collection.find_one({"id":id})
    return row is not None

def insertCode(code):
    global collection
    collection.insert_one(code)


