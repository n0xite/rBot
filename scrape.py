import requests
import logger
from fake_useragent import UserAgent
from selectolax.parser import HTMLParser


# HTMLParser(r.text).css('#pnxssr_9c6268f14883e9e2a70040628b28a8a7 > app-multipanels:nth-child(1) >
# section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(4) > li:nth-child(1)')[0].text()


class Scrape:
    s = requests.Session()
    def addressResolver(self, url, resolve):
        search_url = url
        for i, r in enumerate(resolve):
            search_url += resolve[i]

        if(self.s.get(search_url, headers={'User-Agent':UserAgent().ie}).status_code == 200):
            logger.log("URL resolved successfully", 0)
            return search_url
        else:
            logger.log("There was an error while resolving the url. Status code returned: " + str(self.s.get(search_url,headers={'User-Agent':UserAgent().firefox}).status_code) + " Searched for: " + search_url, 2)



    def crawler(self, url, selector):
        response = self.s.get(url, headers={'User-Agent': UserAgent().chrome})
        if(response.text):
            logger.log('Response received from url: ' + url, 0)
            if(selector != 0):
                on_site_selector = HTMLParser.html(response.text).css(selector)[0]
                text = on_site_selector.text().replace("\\n", "")
                return on_site_selector, text
            else:
                logger.log('Selector is empty, possibly a mistake', 1)
                pass














