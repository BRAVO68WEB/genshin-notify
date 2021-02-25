require('dotenv').config()

const MongoClient = require('mongodb').MongoClient;

async function getTweets(){

    var conn = await MongoClient.connect(process.env.MONGO_CONN);
    var db = conn.db(process.env.MONGO_DB);

    var tweets = await db.collection(process.env.MONGO_COLL_TWEETS).find({}).toArray();

    conn.close();

    return tweets;
  
}   

async function saveTweet(tweet){

    var conn = await MongoClient.connect(process.env.MONGO_CONN);
    var db = conn.db(process.env.MONGO_DB);

    await db.collection(process.env.MONGO_COLL_TWEETS).insertOne(tweet);
    conn.close();

}

module.exports = {
    getTweets:getTweets,
    saveTweet:saveTweet
}