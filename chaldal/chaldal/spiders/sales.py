# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class SalesSpider(scrapy.Spider):
    name = 'sales'
    allowed_domains = ['chaldal.com']
    # start_urls = ['https://chaldal.com/facial-care']

    script = '''
        function main(splash)
            local num_scrolls = 10
            local scroll_delay = 20.0

            local scroll_to = splash:jsfunc("window.scrollTo()")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            assert(splash:go(splash.args.url))
            splash:wait(splash.args.wait)

            for _ = 1, num_scrolls do
                scroll_to(0, get_body_height())
                splash:wait(scroll_delay)
            end        
            return splash:html()
        end
    '''

    def start_requests(self):
        # yield scrapy.Request(url='https://chaldal.com/female-bath', callback=self.parse , headers= {
        #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        # })
        yield SplashRequest( url = "https://chaldal.com/female-bath" , callback = self.parse , endpoint = 'execute' , args = {
            'wait':10,
            'lua_source': self.script
        })

    def parse(self, response):
        for product in  response.xpath("//div[@class='product' or contains(@class,'Subtext')]"):
            yield {
                'Name' : product.xpath(".//div/div[2]/text()").get()
            }
