import logging
from Telegram import client as BotAPI

def parse(data):
    
    msgType = data["type"]

    if(msgType == "message"):
        channel = data["channel"]
        message = data["data"]

        if channel == "codes":
            logging.info("Notification 'Code' received")
            BotAPI.notifyCode(message)
            logging.info("Notified to all users")

        if channel == "tweets":
            logging.info("Notification 'Tweet' received")
            BotAPI.notifyTweet(message)
            logging.info("Notified to all users")

        if channel == "videos":
            logging.info("Notification 'Video' received")
            BotAPI.notifyVideo(message)
            logging.info("Notified to all users")
