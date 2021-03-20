from Telegram.Bot.bot import startBot, sendCode, sendTweet, sendVideo
from Subscribes import Subscribes

def start(token):
    startBot(token)

def notifyCode(code):
    sendCode(code)

def notifyTweet(tweet):
    sendTweet(tweet)

def notifyVideo(video):
    sendVideo(video)
