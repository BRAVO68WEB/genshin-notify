import logging
import json
from Telegram import client as BotAPI

def parse(data):
    
    msgType = data["type"]

    if(msgType == "message"):
        channel = data["channel"]
        message = json.loads(data["data"])

        if channel == "codes":
            logging.info("[%s] - Notification 'Code' received",message["id"])
            BotAPI.notifyCode(message)
            logging.info("[%s] - Notified all users",message["id"])

        if channel == "tweets":
            logging.info("[%s] - Notification 'Tweet' received",message["id"])
            BotAPI.notifyTweet(message)
            logging.info("[%s] - Notified all users",message["id"])

        if channel == "videos":
            logging.info("[%s] - Notification 'Video' received",message["id"])
            BotAPI.notifyVideo(message)
            logging.info("[%s] - Notified all users",message["id"])
