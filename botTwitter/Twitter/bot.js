
const {TwitterClient} = require("twitter-api-client");

const twitterClient = new TwitterClient({
    apiKey: process.env.TWITTER_API_KEY,
    apiSecret: process.env.TWITTER_API_SECRET,
    accessToken: process.env.TWITTER_ACCESS_TOKEN,
    accessTokenSecret: process.env.TWITTER_ACCESS_SECRET
});

function tweet(id,status){

    twitterClient.tweets.statusesUpdate({status:status})
    .then(x => {
        console.log(`[${id}] - Tweeted`);
    })
    .catch(x => {
        console.error(`[${id}] - There was an error on tweet`, x);
    });

}

function retweet(id){
    twitterClient.tweets.statusesRetweetById({id:id})
    .then(x => {
        console.log(`[${id}] - Retweeted`)
    })
    .catch(x => {
        console.error(`[${id}] - There was an error on retweet`, x);
    });
}

function like(id){
    twitterClient.tweets.favoritesCreate({id:id})
    .then(x => {
        console.log(`[${id}] - Liked`)
    })
    .catch(x => {
        console.error(`[${id}] - There was an error on like`, x);
    });
}

module.exports = {
    like:like,
    tweet:tweet,
    retweet:retweet
}