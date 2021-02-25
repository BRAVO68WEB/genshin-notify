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

function retweetOfficial(message){
    let id = message.id;
    retweet(id);
}

module.exports = {
    retweetOfficial:retweetOfficial,
    tweetCode: tweetCode
}
