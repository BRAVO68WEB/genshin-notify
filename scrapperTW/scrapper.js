require("dotenv").config();

const TwitterClient = require("./Twitter/client");
const MongoClient = require("./Mongo/client.js");
const RedisClient = require("./Redis/client.js");

async function scrapper(){

    console.log("Running scrapper");

    let newTweets = _getNewTweets();
    
    try{
        tweets = await newTweets;
    } catch (e){
        console.error("There was an error extracting tweets", e);
        return;
    }

    tweets = tweets.map(x => {
        let url = `https://www.twitter.com/${process.env.TWITTER_ACCOUNT}/status/${x.id_str}`;
        return {"id":x.id_str, "url":url, "user":x.user.screen_name}
    });

    for (tweet of tweets){
        
        if (await MongoClient.existTweet(tweet.id)) {
            continue;
        } else {
            console.log(`[${tweet.id}] - New tweet detected`)
            RedisClient.sendTweet(tweet);
            console.log(`[${tweet.id}] - Notification sent`)
            MongoClient.insertTweet(tweet);
            console.log(`[${tweet.id}] - Saved on Mongo`)

        }

    }

    console.log("Scrapper finished")

}

function _getNewTweets(){
    return TwitterClient.getLastOfficialTweets();
}

module.exports = scrapper;