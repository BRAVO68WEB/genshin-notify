import logging
import redis

redisClient  = None

def start(host, port):
    global redisClient
    redisClient = redis.Redis(host=host, port=port, decode_responses=True)
    logging.info("Connected to Redis")

def sendCode(code):
    redisClient.publish("codes", code)


