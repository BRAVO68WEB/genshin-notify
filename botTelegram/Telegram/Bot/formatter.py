import logging

def video(video):
    url = "https://www.youtube.com/watch?v={}".format(video["id"])

    msg = ("*New video uploaded by {}\!*\n"
    "\n"
    "See it now [here]({})\n"
    "\n"
    ).format(video["channel_title"],url)

    return msg    

def code(code):
    msg = ("*New code available\!*\n"
    "__Reward:__ {}\n"
    "\n"
    "*EU:* {}\n"
    "*NA:* {}\n"
    "*SEA:* {}\n"
    "\n"
    "Redeem right now [here](https://genshin.mihoyo.com/en/gift)\n"
    "\n"
    ).format(code["rewards"],code["eu"],code["na"],code["sea"])

    return msg

def tweet(tweet):
    msg = ("*New tweet by {} *\n"
    "\n"
    "See it [here]({})\n"
    ).format(tweet["user"], tweet["url"])

    return msg
    
def start():
    msg = ("Welcome to Genshin Notify\n"
    "\n"
    "Actually there are two commands that you must know\n"
    "/subscribe -> You subscribe so the bot will notify you when a new code appears\n"
    "/unsubscribe -> Unsubscribe. The bot will not notify you about new codes\n"
    )

    return msg