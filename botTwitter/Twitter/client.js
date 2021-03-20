const {tweet, retweet} = require("./bot");

function tweetCode(message){

    var status = `New code available!\n` +
    `\n` +
    `Rewards: ${message.Rewards}\n` +
    `EU: ${message.EU}\n` +
    `NA: ${message.NA}\n` +
    `SEA: ${message.SEA}\n` +
    `\n` +
    `Redeem it here https://genshin.mihoyo.com/en/gift`;

    tweet(status);

}

function tweetVideo(message){

    var status = `New video from ${message.channel_title}!\n` +
    `\n` +
    `https://www.youtube.com/watch?v=${message.id}`;
    tweet(status);

}

function retweetOfficial(message){
    let id = message.id;
    retweet(id);
}


module.exports = {
    retweetOfficial:retweetOfficial,
    tweetVideo: tweetVideo,
    tweetCode: tweetCode
}
