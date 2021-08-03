import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys

sys.path.append('../')


from chaldal_description.spiders.dove import DoveSpider

process = CrawlerProcess( get_project_settings() )
process.crawl( DoveSpider )
process.start()
