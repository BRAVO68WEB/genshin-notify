require('dotenv').config()

const RedisClient = require("./Redis/client");

RedisClient.start();
