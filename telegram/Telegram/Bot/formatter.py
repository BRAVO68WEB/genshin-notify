import json

def code(code):
    code = json.loads(code)

    msg = ("*New code available\!*\n"
    "__Reward:__ {}\n"
    "\n"
    "*EU:* {}\n"
    "*NA:* {}\n"
    "*SEA:* {}\n"
    "\n"
    "Redeem right now [here](https://genshin.mihoyo.com/en/gift)\n"
    "\n"
    ).format(code["Rewards"],code["EU"],code["NA"],code["SEA"])

    return msg

def tweet(tweet):
    tweet = json.loads(tweet)

    msg = ("*New official tweet*\n"
    "\n"
    "See it [here]({})\n"
    ).format(tweet["url"])

    return msg
    
def start():
    msg = ("Welcome to Genshin Notify\n"
    "\n"
    "Actually there are two commands that you must know\n"
    "/subscribe -> You subscribe so the bot will notify you when a new code appears\n"
    "/unsubscribe -> Unsubscribe. The bot will not notify you about new codes\n"
    )

    return msg