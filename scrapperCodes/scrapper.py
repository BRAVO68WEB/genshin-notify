from bs4 import BeautifulSoup
import json
import logging
import requests

from Mongo import client as MongoClient
from Redis import client as RedisClient

WEB = 'https://www.gensh.in/events/promotion-codes'

class RequestErrorException(Exception):
    def __init__(self, message, resp):
        super().__init__(message)
        self.resp = resp
        self.message = message


def scrapper():
    logging.info("Running scrapper")

    try:
        codes = _scrapCodes()
    except RequestErrorException as e:
        logging.warning("%s\nStatus code %s", e.message, e.resp.status_code)
        return

    for code in codes:

        if MongoClient.existCode(code["id"]):
            continue
        else:
            logging.info("[%s] - New code detected",code["id"])
            RedisClient.sendCode(json.dumps(code))
            logging.info("[%s] - Notification sent",code["id"])
            MongoClient.insertCode(code)
            logging.info("[%s] - Saved on Mongo",code["id"])

    logging.info("Scrapper finished")

def _scrapCodes():

    resp = requests.get(WEB)

    if not resp:
        raise RequestErrorException(resp=resp,message="There was an error on the request")

    source = resp.text
    soup = BeautifulSoup(source, 'lxml')
    table = soup.find('table')

    headers = [heading.text for heading in table.find_all('th')]

    table_rows = [row for row in table.find_all('tr')]

    results = [{headers[index] : cell.text for index,cell in enumerate(row.find_all('td')) } for row in table_rows]

    while {} in results:
        results.remove({})

    results = list(map(_formatter,results))
    
    codes = []
    for result in results:
        code = {
            "id":result["NA"],
            "date_added":result["Date Added"],
            "rewards":result["Rewards"],
            "expired":result["Expired"],
            "eu":result["EU"],
            "na":result["NA"],
            "sea":result["SEA"]
        }
        codes.append(code)

    return codes

def _formatter(result):
    result = {x.strip(): v.strip()
        for x, v in result.items()}
    return result