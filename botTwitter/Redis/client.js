const redis = require("redis");
const TwitterClient = require("../Twitter/client");

function start(){

    const redis = require("redis");
    const subscriber = redis.createClient(
        parseInt(process.env.REDIS_PORT),
        process.env.REDIS_HOST
    );

    subscriber.on("message", function(channel, message) {
        message = JSON.parse(message);
        parse(channel,message);
    });
    
    subscriber.subscribe("codes");
    subscriber.subscribe("tweets");
    subscriber.subscribe("videos")
    
    console.log("Connected to Redis")

}

function parse(channel, message){
    if(channel == "codes"){
        console.log(`[${message.id}] - Notification 'Code' received`);
        TwitterClient.tweetCode(message);
    }

    if(channel == "tweets"){
        console.log(`[${message.id}] - Notification 'Tweet' received`);
        TwitterClient.shareTweet(message);
    }

    if(channel == "videos"){
        console.log(`[${message.id}] - Notification 'Video' received`);
        TwitterClient.tweetVideo(message);
    }

}

module.exports = {
    start:start
}