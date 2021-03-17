require("dotenv").config();

const TwitterClient = require("./Twitter/client");
const MongoClient = require("./Mongo/client.js");
const RedisClient = require("./Redis/client.js");

async function scrapper(){

    console.log("Running scrapper");

    let oldTweets = getOldTweets();
    let newTweets = getNewTweets();

    try{
        oldTweets = await oldTweets;
        newTweets = await newTweets;
    } catch (e){
        console.error("There was an error extracting tweets", e);
        return;
    }

    newTweets = newTweets.map(x => {
        let url = `https://www.twitter.com/${process.env.TWITTER_ACCOUNT}/status/${x.id_str}`;
        return {"id":x.id_str, "url":url}
    });

    let tweets = checkNewTweets(oldTweets,newTweets);
    
    if(tweets.length != 0){
        console.log("New tweets found");
        console.log("Sending notifications");
        for (tweet of tweets){
            try{ 
                RedisClient.publish(tweet);
                MongoClient.saveTweet(tweet);
            } catch (e){
                console.error("There was saving/publishing tweets", e);
                return;
            }
        }
        console.log("All notifications sent");
    } else {
        console.log("No new tweets found");
    }

}

function getOldTweets(){
    return MongoClient.getTweets();
}

function getNewTweets(){
    return TwitterClient.getLastOfficialTweets();
}

function checkNewTweets(oldTweets,newTweets){

    return newTweets.filter(x => {
        return !oldTweets.some(y => y.id === x.id);
    });

}

module.exports = scrapper;