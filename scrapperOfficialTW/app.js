require('dotenv').config()

const cron = require('node-cron');
const scrapper = require('./scrapper');

console.log("Starting scrapper");

cron.schedule('* * * * *', function() {
    scrapper();
});