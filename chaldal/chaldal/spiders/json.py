# -*- coding: utf-8 -*-
import scrapy
import json
import pprint

class JsonSpider(scrapy.Spider):
    name = 'json'
    allowed_domains = ['chaldal.com']

    def start_request( self ):
        yield scrapy.Request(url = "https://catalog.chaldal.com/searchOld" , callback = self.parse_id)
    
    def parse_id( self , response ):
        data = json.loads( response.body )
        # printer = pprint.PrettyPrinter()
        # printer.pprint( data )
        with open( 'sample.json' , 'w' ) as file:
            file.write( json.dumps( data ) )

    def parse(self, response):
        pass
