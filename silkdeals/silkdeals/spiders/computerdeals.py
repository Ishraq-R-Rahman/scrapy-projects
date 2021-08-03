# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'

    def remove_characters( self , value ):
        return value.strip('\xa0') 

    def start_requests(self):
        yield SeleniumRequest (
            url = 'https://slickdeals.net/computer-deals/', 
            wait_time = 3,
            callback = self.parse
        )   

    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals']/li")
        for product in products:
            yield {
                'name': product.xpath(".//a[contains(@class,'itemTitle')]/text()").get(),
                'link': product.xpath(".//a[contains(@class,'itemTitle')]/@href").get(),
                'Store-name': self.remove_characters( product.xpath("normalize-space(.//span[contains(@class,'blueprint') or contains(@class , 'itemStore')])").get() ),
                'Price': product.xpath("normalize-space(.//div[contains(@class,'itemPrice')]/text())").get(),
                'user-agent': response.request.headers.get('User-Agent').decode('utf-8')
            }


        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            absolute_url = f"https://slickdeals.net{next_page}"
            yield SeleniumRequest( url = absolute_url , wait_time = 3, callback = self.parse)
