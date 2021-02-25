from Telegram.Bot.bot import startBot, sendCode, sendTweet
from Subscribes import Subscribes

def start(token):
    startBot(token)

def notifyCode(code):
    sendCode(code)

def notifyOfficialTW(tweet):
    sendTweet(tweet)
