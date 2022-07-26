from datetime import datetime
from scrapy_selenium import SeleniumRequest

from compasscraper.items import ShopeeItem

from scrapy.spiders import CrawlSpider


class ShopeeSpider(CrawlSpider):
    name = 'shopeesukanda'
    start_urls = ['https://shopee.co.id/sukandahome']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'FileCrawled/Shopee/shopeesukanda_{}.csv'.format(int(datetime.now().strftime('%Y%m%d')))
    }

    def start_requests(self):
        # todo add expected condition to make sure all page loaded completely
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse_product,
                wait_time=6
            )

    def parse_product(self, response):
        item = ShopeeItem()
        all_product = response.css(
            'div[class="shop-search-result-view__item col-xs-2-4"]'
        )
        for product in all_product:
            nama = product.css('div[class="_3Gla5X _2j2K92 _3j20V6"] ::text').extract_first()
            harga = product.css('span[class="_3TJGx5"] ::text').extract_first()
            alamat = product.css('div[class="_1IbMik"] ::text').extract_first()
            terjual = product.css('div[class="_2Tc7Qg _2R-Crv"] ::text').extract_first()
            item['nama'] = nama
            item['harga'] = harga
            item['alamat'] = alamat
            item['terjual'] = terjual
            item['url'] = ''
            yield item






