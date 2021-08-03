# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class SQLlite3Pipeline(object):
    
    # @classmethod
    # def from_crawler( cls , crawler ):


    def open_spider( self , spider ):
        self.connection = sqlite3.connect("imdb.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute(
            '''
                CREATE TABLE best_movies( 
                    title TEXT,
                    year TEXT,
                    genre TEXT,
                    duration TEXT,
                    rating TEXT,
                    movie_url TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider( self , spider ):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute(
            '''
                INSERT INTO best_movies ( title , year , genre , duration , rating, movie_url ) VALUES ( ?, ? ,? ,? ,? ,? )
            '''
        , (
            item.get('title'),
            item.get('year'),
            item.get('genre'),
            item.get('duration'),
            item.get('rating'),
            item.get('movie_url')
        ))
        self.connection.commit()
        return item
