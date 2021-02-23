import logging
import redis
from Redis.parser import parse

def start(host, port):

    r = redis.Redis(host=host, port=port, decode_responses=True)
    logging.info("Connected to Redis")

    p = r.pubsub()
    p.subscribe("codes","leaks","notices","official","updates")

    listen(p)

def listen(p):
    for message in p.listen():
        parse(message)
