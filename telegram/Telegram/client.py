from Telegram.Bot.bot import startBot, sendCode
from Subscribes import Subscribes

def start(token):
    startBot(token)

def notifyCode(code):
    sendCode(code)
