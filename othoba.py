import scrapy


class OthobaSpider(scrapy.Spider):
    name = 'othoba'
    allowed_domains = ['www.othoba.com/src?q=ponds']
    start_urls = ['http://www.othoba.com/src?q=ponds/']

    def parse(self, response):
        pass
