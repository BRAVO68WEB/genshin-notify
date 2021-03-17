
from Mongo import client as MongoClient
from Subscribes.Exceptions import AlreadySubscribedException, NotSubscribedException

def sub(chat_id):

    if MongoClient.userExists(chat_id):
        raise AlreadySubscribedException
    else:
        MongoClient.addUser(chat_id)

def unsub(chat_id):

    if not MongoClient.userExists(chat_id):
        raise NotSubscribedException
    else:
        MongoClient.removeUser(chat_id)

def listAll():
    return MongoClient.listAll()
