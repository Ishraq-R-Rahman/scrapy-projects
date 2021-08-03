# -*- coding: utf-8 -*-
import scrapy
import os


class DoveSpider(scrapy.Spider):
    print("***********************************************************************************")
    if( os.environ.get('START_URLS') is None ) :
        url = 'https://chaldal.com/search/dove'
    else :
        url = os.environ.get('START_URLS').split(',')
    print(url)
    print("***********************************************************************************")


    name = 'dove'
    allowed_domains = ['chaldal.com']
    start_urls = url

    def parse(self, response):
        

        urls = response.xpath("//div[@class='overlay text']/span/a[1]")
        
        for val in urls:
            url = response.urljoin( val.xpath(".//@href").get() ) 
            yield response.follow( url = url , callback = self.parse_description )

    def parse_description( self , response ):
        # print("*****************")
        # print(response.url)
        # if "dove" in response.url :
        #     print("12345678754321345465786")
            
        if( response.xpath("//div[@class='outOfStockBtn']").getall() ):
            instock = "Out of Stock"
        else :
            instock = "In stock"

        # Have to check if the names contain the search tag, otherwise includes unrelated products
        name = response.xpath("//div[@class='nameAndSubtext']/h1/text()").get() 
        if( "Pond" not in name and "Dove" not in name ):
            return
        
        yield {
            'Name' : name,
            'Size' : response.xpath("//div[@class='nameAndSubtext']/span/text()").get(),
            'Final Price' : response.xpath("//span[@itemprop='price']/span/text()").get(),
            'Price Without Discount': response.xpath("//div[@class='fullPrice']/span[2]/text()").get(),
            'Stock' : instock,
            'Description': response.xpath("//div[@itemprop='description']/p/text()").getall(),
            'Image' : response.xpath("//img[@itemprop='image']/@src").get()
        }      
