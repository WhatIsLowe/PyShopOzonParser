import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from ..items import SmartphoneItem


class OzonSpider(scrapy.Spider):
    name = "ozon"
    allowed_domains = ["ozon.ru"]
    start_urls = ["https://www.ozon.ru/category/smartfony-15502/?page=1"]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        selector = Selector(text=self.driver.page_source)
        phones = selector.xpath('//div[@class="title"]')    # TODO: изменить xpath адреса
        for phone in phones:
            link = phone.xpath('.//a/@href').get()
            yield scrapy.Request(url=link, callback=self.parse_phone_info)

    def parse_phone_info(self, response):
        # TODO: Реализовать парсинг страницы с информацией о смартфоне
        pass
