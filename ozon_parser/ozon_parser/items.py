# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmartphoneItem(scrapy.Item):
    manufacturer = scrapy.Field()
    model = scrapy.Field()
    os_version = scrapy.Field()
