import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from worldometers.worldometers.spiders.countries import CountriesSpider


process = CrawlerProcess( get_project_settings(), {
    'FEED_FORMAT': 'json',
    'FEED_URI': 'country.json'
} )
process.crawl( CountriesSpider )
process.start()
print("****************************************************************************")
print( get_project_settings().attributes['BOT_NAME'] )
