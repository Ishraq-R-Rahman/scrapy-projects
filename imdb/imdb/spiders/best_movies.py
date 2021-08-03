# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    # start_urls = ['https://www.imdb.com/chart/top/']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    def start_requests( self ):
        yield scrapy.Request( url = 'https://www.imdb.com/chart/top/' , headers={
            'User-Agent':self.user_agent
        } )

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'), callback='parse_item', follow=True , process_request = 'set_user_agent'),
    )

    def set_user_agent( self , request ):
        request.headers['User-Agent']= self.user_agent
        return request

    def parse_item(self, response):
        # print(response.url)
        yield {
            'title' : response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year' : response.xpath("//span[@id='titleYear']/a/text()").get(),
            'genre' : response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'duration' : response.xpath("//time[1]/text()").get().strip(),
            'rating' : response.xpath("//div[@class='subtext']/text()").get().strip(),
            'movie_url' : response.url,
            'User-Agent' : response.request.headers['User-Agent']
        }
