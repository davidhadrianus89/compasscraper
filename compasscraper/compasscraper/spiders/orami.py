from datetime import datetime
import pandas as pd

from scrapy_selenium import SeleniumRequest
from scrapy import Spider


def get_product_url():
    data = pd.read_csv("/home/david/Desktop/compasscraper/url_product.csv")
    urls = data['urls']
    urls_ = []
    for row in urls:
        urls_.append(row)
    return urls


urls = get_product_url()


class OramiSpider(Spider):
    name = 'orami'
    url = urls
    #start_urls = url
    start_urls = ["https://www.orami.co.id/shopping/product/buy-2-slim-fit-meal-replacement-french-vanila-get-1-tas-gym", ""]

    # custom_settings = {
    #     'FEED_FORMAT': 'csv',
    #     'FEED_URI': 'FileCrawled/Orami/orami.csv'.format(int(datetime.now().strftime('%Y%m%d')))
    # }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=3)

    def parse(self, response):
        harga = response.css(
            'h3[class="jsx-1894068073 text-coral text is-size-h5 is-font-modern-era-bold prod-detail-price m-0 "]  ::text').extract()[1].strip()
        nama = response.css(
            'h1[class="jsx-1894068073 text is-size-deci is-font-modern-era-bold align-left text-charcoal-700 m-0 "]  ::text').extract()[0].strip()

        stock = response.css(
            'div[class="jsx-1894068073 d-flex prod-detail-stock "]  ::text').extract()[
            0].strip()

        seller = response.css(
            'div[class="jsx-3646570757 text-charcoal-700 text is-size-small is-weight-bold "]  ::text').extract()[
            0].strip()
        brand = response.css(
            'tbody[class="prod-detail-spesification"]  ::text').extract()
        print("NAMA", nama, harga, stock, seller, brand)

