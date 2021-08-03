# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape'
    allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['https://quotes.toscrape.com/js/']

    script = '''
        function main(splash, args)
            --splash.private_mode_enabled = false
            url = args.url
            assert( splash:go(url) )
            assert( splash:wait(1) )
            
            
            --splash:set_viewport_full()
            return splash:html()
        end
    '''

    def start_requests( self ):
        yield SplashRequest( url = "https://quotes.toscrape.com/js/" , callback = self.parse , endpoint = 'execute' , args = {
            'lua_source': self.script
        })

    def parse(self, response):

        for quotes in response.xpath("//div[@class='quote']"):
            yield {
                'Quote': quotes.xpath(".//span[1]/text()").get(),
                'Author': quotes.xpath(".//span[2]/small/text()").get(),
                'Tags': quotes.xpath(".//div/a/text()").getall()
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        # print(response.urljoin(next_page) )
        
        if next_page:
            absolute_url = f"https://quotes.toscrape.com{next_page}"
            yield SplashRequest( url = absolute_url , callback = self.parse , endpoint='execute', args ={
                'lua_source': self.script
            })
