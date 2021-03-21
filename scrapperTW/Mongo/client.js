require('dotenv').config()

const MongoClient = require('mongodb').MongoClient;

const MONGO_CONN = process.env.MONGO_CONN
const MONGO_DB = process.env.MONGO_DB
const COLLECTION = process.env.MONGO_COLL_TWEETS

async function existTweet(id){

    var conn = await MongoClient.connect(MONGO_CONN);
    var db = conn.db(MONGO_DB);

    var row = await db.collection(COLLECTION).findOne({id:id});
    conn.close();

    return row != null;
    
}

async function insertTweet(tweet){

    var conn = await MongoClient.connect(MONGO_CONN);
    var db = conn.db(MONGO_DB);

    await db.collection(COLLECTION).insertOne(tweet);
    conn.close();

}

module.exports = {
    existTweet:existTweet,
    insertTweet:insertTweet
}