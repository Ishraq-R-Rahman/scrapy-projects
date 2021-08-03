# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookListSpider(CrawlSpider):
    name = 'book_list'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/', headers={
            'User-Agent': self.user_agent
        })

    

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback='parse_item', follow=True , process_request= 'set_user_agent'),
        Rule( LinkExtractor( restrict_xpaths="//li[@class='next']/a" ) , process_request= 'set_user_agent'),
    )

    def set_user_agent( self , request ):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//p[@class='price_color']/parent::node()/h1/text()").get(),
            'price': response.xpath("//p[@class='price_color']/text()").get()
            # 'User_Agent': response.request.headers['User-Agent']
        }
