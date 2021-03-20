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
    
}

function parse(channel, message){
    if(channel == "codes"){
        console.log("Notification 'Code' received");
        TwitterClient.tweetCode(message);
    }

    if(channel == "tweets"){
        console.log("Notification 'Tweet' received");
        TwitterClient.retweetOfficial(message);
    }

    if(channel == "videos"){
        console.log("Notification 'Video' received");
        TwitterClient.tweetVideo(message);
    }

}

module.exports = {
    start:start
}