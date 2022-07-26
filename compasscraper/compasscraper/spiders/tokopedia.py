from datetime import datetime
from scrapy_selenium import SeleniumRequest
from scrapy import Spider


from compasscraper.spiders.utils import ExpectedConditionModifier


class TokopediaSpider(Spider):
    name = 'tokopediasukanda'
    url = ['https://www.tokopedia.com/sukandahome']
    start_urls = url

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'FileCrawled/Tokopedia/tokopediasukanda_{}.csv'.format(int(datetime.now().strftime('%Y%m%d')))
    }

    def start_requests(self):
        # todo add expected condition to make sure all page loaded completely
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=8
            )


    def parse(self, response):
        all_products = response.css(
            'div[class="css-1sn1xa2"]'
        )
        for a in all_products:
            pass