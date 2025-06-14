# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeItem(scrapy.Item):
    house = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    total = scrapy.Field()
