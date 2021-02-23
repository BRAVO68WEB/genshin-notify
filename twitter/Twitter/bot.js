
const {TwitterClient} = require("twitter-api-client");

const twitterClient = new TwitterClient({
  apiKey: process.env.TWITTER_API_KEY,
  apiSecret: process.env.TWITTER_API_SECRET,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessTokenSecret: process.env.TWITTER_ACCESS_SECRET
});

function tweet(status){

  twitterClient.tweets.statusesUpdate({status:status})
    .then(x => {
      console.log("Tweeted!");
    })
    .catch(x => {
      console.error("There was an error on publishing tweet", x);
    });
}

module.exports = {
  tweet:tweet
}