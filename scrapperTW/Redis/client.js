require('dotenv').config()

const redis = require("redis");

function sendTweet(tweet){

    const redis = require("redis");
    const client = redis.createClient(
        parseInt(process.env.REDIS_PORT),
        process.env.REDIS_HOST
    );

    client.publish("tweets",JSON.stringify(tweet));
    
    client.quit();

}

module.exports = {
    sendTweet:sendTweet
}