from datetime import datetime
from scrapy_selenium import SeleniumRequest
from scrapy import Spider
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapy.spiders import CrawlSpider


class ShopeeSpider(CrawlSpider):
    name = 'shopeesukanda'
    start_urls = ['https://shopee.co.id/sukandahome']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'FileCrawled/Shopee/shopeesukanda_{}.csv'.format(int(datetime.now().strftime('%Y%m%d')))
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url,
                          callback=self.parse_product,
                          wait_time=3,
                          )

    def parse_product(self, response):
        print(response.url)






