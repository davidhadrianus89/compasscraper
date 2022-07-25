from datetime import datetime
from scrapy_selenium import SeleniumRequest
from scrapy import Spider


class TokopediaSpider(Spider):
    name = 'tokopediasukanda'
    url = ['https://www.tokopedia.com/sukandahome']
    start_urls = url

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'FileCrawled/Tokopedia/tokopediasukanda.csv'.format(int(datetime.now().strftime('%Y%m%d')))
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=3
            )

    def parse(self, response):
        print(response.text)
