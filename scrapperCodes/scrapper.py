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


def scrapper():
    logging.info("Running scrapper")
    old_codes = getOldCodes()

    try:
        scrap_codes = scrapCodes()
    except RequestErrorException as e:
        logging.warning("%s\nStatus code %s", e.message, e.resp.status_code)
        return
        
    new_codes = checkNewCodes(scrap_codes,old_codes)
    if new_codes != []:
        for code in new_codes:
            logging.info("New code detected")
            RedisClient.sendCode(json.dumps(code))
            logging.info("Notification sent")
        MongoClient.insertCodes(new_codes)
        logging.info("Saved new codes on Mongo")
    else:
        logging.info("No new code detected")

def scrapCodes():

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
    
    return results

def getOldCodes():
    old_codes = list(MongoClient.listAllCodes())
    return old_codes

def checkNewCodes(scrap_codes,old_codes):

    check_codes = [old_codes[index]['EU'] for index, i in enumerate(old_codes)]

    new_codes = []

    for scrap_code in scrap_codes:
        if scrap_code['EU'] not in check_codes:
            new_codes.append(scrap_code)    
    
    return new_codes

def _formatter(result):
    result = {x.strip(): v.strip()
        for x, v in result.items()}
    return result