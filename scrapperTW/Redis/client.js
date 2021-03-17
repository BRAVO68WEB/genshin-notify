require('dotenv').config()

const redis = require("redis");

function publish(tweet){

    const redis = require("redis");
    const client = redis.createClient(
        parseInt(process.env.REDIS_PORT),
        process.env.REDIS_HOST
    );

    client.publish("officialTW",JSON.stringify(tweet));
    
    client.quit();

}

module.exports = {
    publish:publish
}