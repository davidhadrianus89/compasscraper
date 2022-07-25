# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompasscraperItem(scrapy.Item):
    nama = scrapy.Field()
    brand = scrapy.Field()
    kategori = scrapy.Field()
    penjual = scrapy.Field()
    harga = scrapy.Field()
    stock = scrapy.Field()
    url = scrapy.Field()
