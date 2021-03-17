require('dotenv').config()

const {TwitterClient} = require("twitter-api-client");

const twitterClient = new TwitterClient({
    apiKey: process.env.TWITTER_API_KEY,
    apiSecret: process.env.TWITTER_API_SECRET,
    accessToken: process.env.TWITTER_ACCESS_TOKEN,
    accessTokenSecret: process.env.TWITTER_ACCESS_SECRET
});

function getLastOfficialTweets(){
    return twitterClient.tweets.statusesUserTimeline({screen_name: "GenshinImpact",include_rts:false});
}

module.exports = {
  getLastOfficialTweets:getLastOfficialTweets
}