import requests
from fake_useragent import UserAgent
import configHandler
from selectolax.parser import HTMLParser
from time import sleep
import logger
import json

# faster alternative for auto.py
# chained request based interaction


class AutomateRequests:
    config = configHandler.read_config('config.ini')
    urlChain = str.split(config.get("SITE","urlChain"))
    s = requests.Session()
    def interact(self):
        delay = int(self.config['APP']['setDelay'])
        r = self.s.get(self.urlChain[0], headers={'User-Agent': UserAgent().chrome})
        html = HTMLParser(r.text).html
        r.cookies
        for i, url in enumerate(self.urlChain):
            response = []
            sleep(delay)
            response += self.s.get(self.urlChain[i], headers={'User-Agent': UserAgent().chrome})


            sleep(delay/4)
        print("Cookies: " + str(r.cookies))
        return r, html

    def input(self, url, data):
        json_data = data
        r = self.s.post(url=url,headers={"content-type": "application/json","user-agent":UserAgent().chrome},data=json_data)
        if r.status_code <= 299:
            logger.log("Data POST request successful. Response: " + r.text,0)

        else:
            logger.log("Response code: " + str(r.status_code) + " URL: " + url + "\n POST data: " + json_data +" Response: " + r.text, 2)
        # add logs

        print("Cookies: " + str(r.cookies))

    def __init__(self):
        r = self.interact(self)
        print("Status: " + str(r[0]))







