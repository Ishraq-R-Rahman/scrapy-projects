# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging 
import pymongo
import sqlite3

class MongodbPipeline(object):
    collection_name = "computer_deals"

    # @classmethod
    # def from_crawler( cls , crawler ):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider( self , spider):
        # logging.warning( "Spider opened from pipeline")
        self.client = pymongo.MongoClient( "mongodb+srv://shwarup:shawroop@cluster0.xo3vj.mongodb.net/cluster0?retryWrites=true&w=majority")
        self.db = self.client["Silkdeal"]

    def close_spider( self , spider ):
        # logging.warning( "Spider closed from pipeline")
        self.client.close()

    def process_item(self, item, spider):
        self.db[ self.collection_name ].insert( item )
        return item


class SQLlitePipeline(object):

    # @classmethod
    # def from_crawler( cls , crawler ):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider( self , spider):
        # logging.warning( "Spider opened from pipeline")
        self.connection = sqlite3.connect("computer_deals.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute(
            '''
                CREATE TABLE COMPUTERS(
                    name TEXT,
                    link TEXT,
                    store_name TEXT,
                    price TEXT
                )
            '''
            )

            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider( self , spider ):
        # logging.warning( "Spider closed from pipeline")
        self.connection.close()

    def process_item(self, item, spider):
        # self.db[ self.collection_name ].insert( item )
        self.c.execute(
         '''
            INSERT INTO COMPUTERS ( name , link , store_name, price ) VALUES( ? , ? ,? , ?)
         '''   
        , ( 
            item.get( 'name' ),
            item.get( 'link' ),
            item.get( 'Store-name' ),
            item.get( 'Price' ),
            
        ) )

        self.connection.commit()
        return item
