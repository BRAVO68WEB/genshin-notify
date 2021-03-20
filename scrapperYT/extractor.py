from dotenv import load_dotenv
import os

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
QUANT_VIDEOS_EXTRACT = os.environ.get("QUANT_VIDEOS_EXTRACT")

CHANNEL_ID = os.environ.get("CHANNEL_ID")

import requests, json, logging
from Mongo import client as MongoClient
from Redis import client as RedisClient

class RequestErrorException(Exception):
    def __init__(self, message, resp):
        super().__init__(message)
        self.resp = resp

def extractVideos():

    logging.info("Running extractor for {}".format(CHANNEL_ID))

    try:
        videos = _getVideos(CHANNEL_ID)
    except RequestErrorException as e:
        logging.warning("%s\nStatus code %s", e.message, e.resp.status_code)
        return

    for video in videos:

        videoJson = {
            "id":video["id"]["videoId"],
            "channel_id":video["snippet"]["channelId"],
            "channel_title":video["snippet"]["channelTitle"],
            "date_published":video["snippet"]["publishedAt"],
            "title":video["snippet"]["title"],
            "description":video["snippet"]["description"]
        }

        if (MongoClient.existVideo(videoJson["id"])):
            break
        logging.info("New video from {} detected - ID: {}".format(CHANNEL_ID,videoJson["id"]))
        RedisClient.sendVideo(json.dumps(videoJson))
        logging.info("Notification sent")
        MongoClient.insertVideo(videoJson)
        logging.info("Saved video on Mongo")

    logging.info("Extractor finished")

def _getVideos(channelId):

    url = "https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}".format(YOUTUBE_API_KEY,channelId,QUANT_VIDEOS_EXTRACT)

    resp = requests.get(url)

    if resp.status_code != 200:
        raise RequestErrorException(resp=resp,message="There was an error on the request")
    
    data = resp.json()

    return data["items"]