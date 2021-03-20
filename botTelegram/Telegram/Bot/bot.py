import logging
from telegram.ext import Updater, CommandHandler
from Telegram.Bot.handlers import handlerStart, handlerSubscribe, handlerUnsubscribe

import Telegram.Bot.formatter as Formatter

from Subscribes import Subscribes

bot = None

def startBot(token):

    global bot
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', handlerStart))
    updater.dispatcher.add_handler(CommandHandler('subscribe', handlerSubscribe))
    updater.dispatcher.add_handler(CommandHandler('unsubscribe', handlerUnsubscribe))

    bot = updater.bot
    logging.info("Connected to Telegram")

    updater.start_polling()

def sendCode(code):
    for sub in Subscribes.listAll():
        bot.send_message(chat_id=sub["chat_id"],text=Formatter.code(code),parse_mode='MarkdownV2')
    
def sendTweet(tweet):
    for sub in Subscribes.listAll():
        bot.send_message(chat_id=sub["chat_id"],text=Formatter.tweet(tweet),parse_mode='MarkdownV2')

def sendVideo(video):
    for sub in Subscribes.listAll():
        bot.send_message(chat_id=sub["chat_id"],text=Formatter.video(video),parse_mode='MarkdownV2')
