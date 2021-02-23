# Genshin Notify
Genshin Impact notifier about notices, leaks and promotion codes on differents platforms (Telegram/Discord/Twitter).

### How to use

- On Telegram: [@GenshinNotifyBot](https://t.me/GenshinNotifyBot)
- On Discord: [@GenshinNotify](https://discord.com/oauth2/authorize?client_id=813534602228269066&permissions=257088&scope=bot)
- On Twitter: [@GenshinNotify](https://twitter.com/GenshinNotify)

### To do

#### Scrappers
- [X] Promotion codes
- [ ] Notices
- [ ] Leaks

#### Configuration
- [ ] Add multi-language support (ES/EN)
    - [ ] on Telegram
    - [ ] on Discord
- [ ] Choose what type of information you want to receive (leaks, notices, promotion codes, ...)
    - [ ] on Telegram
    - [ ] on Discord
    
#### Bots
- [X] Telegram bot
- [ ] Twitter bot
- [ ] Discord bot

### How to run local

1. Create the .env files based on .env.template (More info in [this section](#env-files))
2. Run the command

```bash
docker compose up
```

### env files

You need to create/edit the following .env files. There are templates uploaded in the corresponding folders.

```bash
# Scrapper .env file

REDIS_HOST=redis
REDIS_PORT=6379

MONGO_CONN=mongodb://mongo:27017
MONGO_DB=genshinNotify
MONGO_COLL=codes
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
