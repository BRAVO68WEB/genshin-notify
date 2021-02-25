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

        if channel == "officialTW":
            logging.info("Notification 'OfficialTW' received")
            BotAPI.notifyOfficialTW(message)
            logging.info("Notified to all users")
