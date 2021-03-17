# Genshin Notify
Genshin Impact notifier about notices, leaks and promotion codes on differents platforms (Telegram/Discord/Twitter).

### How to use (for clients/players)

- On Telegram: [@GenshinNotifyBot](https://t.me/GenshinNotifyBot) - [Tutorial](documents/how_to_use/telegram.md)
- On Discord: [@GenshinNotify](https://discord.com/oauth2/authorize?client_id=813534602228269066&permissions=257088&scope=bot) - [Tutorial](documents/how_to_use/telegram.md)
- On Twitter: [@GenshinNotify](https://twitter.com/GenshinNotify) - [Tutorial](documents/how_to_use/telegram.md)

### Description

There are three bots (Telegram, Discord and Twitter) that will notify you when there are news, leaks or promotion codes in the Genshin Impact Game. The format of the notification and configurations depends on the platform used... 

##### Twitter
- Retweets from official account [@GenshinImpact](https://twitter.com/GenshinNotify)
- Tweets when new code is published in [gensh.in](https://www.gensh.in/)

##### Telegram
*If you are subscribed to the bot with the command* ***/subscribe***
- Send a message when a new tweet is published from the official account [@GenshinImpact](https://twitter.com/GenshinNotify)
- Send a message when new code is published in [gensh.in](https://www.gensh.in/)

##### Discord
- TODO

### TODO

##### Scrappers
- [X] Promotion codes
- [X] Notices
- [ ] Leaks

##### Configuration
- [ ] Add multi-language support (ES/EN)
    - [ ] on Telegram
    - [ ] on Discord
- [ ] Choose what type of information you want to receive (leaks, notices, promotion codes, ...)
    - [ ] on Telegram
    - [ ] on Discord

##### Bots
- [X] Telegram bot
- [X] Twitter bot
- [ ] Discord bot

### How to run local (for devs)

1. Create the .env files based on .env.template (More info in [this section](#env-files))
2. Run the command

```bash
docker-compose up -d --build
```

### env files

You need to create/edit the following .env files. There are templates uploaded in the corresponding folders.

```bash
# Scrapper Codes .env file

REDIS_HOST=redis
REDIS_PORT=6379

MONGO_CONN=mongodb://mongo:27017
MONGO_DB=genshinNotify
MONGO_COLL=codes

REPEAT_SCRAP_IN_MINUTES=10
```

```bash
# Scrapper Official TW .env file

TWITTER_API_KEY=<YOUR_TWITTER_APP_API_KEY>
TWITTER_API_SECRET=<YOUR_TWITTER_APP_SECRET_KEY>
TWITTER_ACCESS_TOKEN=<YOUR_TWITTER_ACCESS_TOKEN>
TWITTER_ACCESS_SECRET=<YOUR_TWITTER_ACCESS_SECRET>

TWITTER_ACCOUNT=<YOUR_TWITTER_ACCOUNT>

REDIS_HOST=redis
REDIS_PORT=6379

MONGO_CONN = mongodb://mongo:27017
MONGO_DB=genshinNotify
MONGO_COLL_TWEETS=officialTweets

QUANT_TWEETS_EXTRACT=10
REPEAT_SCRAP_IN_MINUTES=5
```

```bash
# Telegram .env file

TELEGRAM_TOKEN=<YOUR_BOT_TOKEN>

REDIS_HOST=redis
REDIS_PORT=6379

MONGO_CONN=mongodb://mongo:27017
MONGO_DB=genshinNotify
MONGO_COLL=telegramSubs
```

```bash
# Twitter .env file

TWITTER_API_KEY=<YOUR_TWITTER_APP_API_KEY>
TWITTER_API_SECRET=<YOUR_TWITTER_APP_SECRET_KEY>
TWITTER_ACCESS_TOKEN=<YOUR_TWITTER_ACCESS_TOKEN>
TWITTER_ACCESS_SECRET=<YOUR_TWITTER_ACCESS_SECRET>

REDIS_HOST=redis
REDIS_PORT=6379
```

