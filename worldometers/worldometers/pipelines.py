# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongodbPipeline(object):

    # collection_name = 'listed_countries'
    
    # def open_spider(self,spider):
    #     # logging.warning("Spider opened from pipeline")
    #     # self.client = pymongo.MongoClient("mongodb+srv://shwarup:shawroop@product.xwfvv.mongodb.net/Countries?retryWrites=true&w=majority")
    #     # self.db = self.client["Countries"]

    # def close_spider(self,spider):
    #     # logging.warning("Spider closed from pipeline")
        # self.client.close()

    def process_item(self, item, spider):
        # self.db[self.collection_name].insert(item)
        return item
