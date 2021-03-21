const {tweet, retweet, like} = require("./bot");

function tweetCode(message){

    var status = `New code available!\n` +
    `\n` +
    `Rewards: ${message.rewards}\n` +
    `EU: ${message.eu}\n` +
    `NA: ${message.na}\n` +
    `SEA: ${message.sea}\n` +
    `\n` +
    `Redeem it here https://genshin.mihoyo.com/en/gift`;

    tweet(message.id,status);

}

function tweetVideo(message){

    var status = `New video from ${message.channel_title}!\n` +
    `\n` +
    `https://www.youtube.com/watch?v=${message.id}`;
    tweet(message.id,status);

}

function shareTweet(message){
    retweet(message.id);
    like(message.id);
}


module.exports = {
    shareTweet:shareTweet,
    tweetVideo: tweetVideo,
    tweetCode: tweetCode
}
