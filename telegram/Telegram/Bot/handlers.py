from Subscribes import Subscribes
from Subscribes.Exceptions import AlreadySubscribedException, NotSubscribedException

import formatter as Formatter

def handlerStart(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=Formatter.start())

def handlerSubscribe(update, context):
    chat_id = update.effective_chat.id
    try:
        Subscribes.sub(chat_id)
        msg = "You subscribed correctly!"
    except AlreadySubscribedException:
        msg = "You are already subscribed!"
    finally:
        context.bot.send_message(chat_id=chat_id, text=msg)

def handlerUnsubscribe(update, context):
    chat_id = update.effective_chat.id
    try:
        Subscribes.unsub(chat_id)
        msg = "You unsubscribed correctly!"
    except NotSubscribedException:
        msg = "You are not subscribed!"
    finally:
        context.bot.send_message(chat_id=chat_id, text=msg)