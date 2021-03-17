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

def userExists(chat_id):
    global collection
    return collection.find_one({"chat_id": chat_id}) is not None

def addUser(chat_id):
    global collection
    user = {"chat_id": chat_id}
    collection.insert_one(user)    

def removeUser(chat_id):
    global collection
    collection.delete_one({"chat_id": chat_id})

def listAll():
    global collection
    return collection.find()