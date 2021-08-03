# -*- coding: utf-8 -*-
import scrapy


class DebttogdpratioSpider(scrapy.Spider):
    name = 'debtToGDPRatio'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")

        for country in countries:
            name = country.xpath(".//td[1]/a/text()").get()
            gdp = country.xpath(".//td[2]/text()").get()

            yield {
                'Country ' : name,
                'National debt to gdp ratio ': gdp
            }
