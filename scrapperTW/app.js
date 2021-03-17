require('dotenv').config()

const cron = require('node-cron');
const scrapper = require('./scrapper');

console.log("Starting scrapper");

REPEAT_SCRAP_IN_MINUTES = process.env.REPEAT_SCRAP_IN_MINUTES

cron.schedule(`*/${REPEAT_SCRAP_IN_MINUTES} * * * *`, function() {
    scrapper();
});