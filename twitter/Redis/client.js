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
    subscriber.subscribe("officialTW");
    
    subscriber.subscribe("leaks");
    subscriber.subscribe("notices");
    subscriber.subscribe("updates");
    
}

function parse(channel, message){
    if(channel == "codes"){
        console.log("Notification 'Code' received!");
        TwitterClient.tweetCode(message);
    }

    if(channel == "officialTW"){
        console.log("Notification 'OfficialTW' received!");
        TwitterClient.retweetOfficial(message);
    }

}

module.exports = {
    start:start
}