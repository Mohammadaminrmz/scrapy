import scrapy


class FirstspiderSpider(scrapy.Spider):
    name = 'firstspider'
    allowed_domains = ['jobinja.ir']
    start_urls = ['http://jobinja.ir/']

    def parse(self, response):
        pass
