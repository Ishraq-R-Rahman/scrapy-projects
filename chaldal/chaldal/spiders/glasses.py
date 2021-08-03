# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        product_list = response.xpath("//div[@id='product-lists']/descendant::div[@class='p-title-block']")
        for product in product_list:
            name = product.xpath(".//descendant::div[@class='p-title']/a/text()").get().strip()
            url = product.xpath(".//descendant::div[@class='p-title']/a/@href").get()
            price = product.xpath(".//descendant::div[@class='p-price']/div/span[1]/text()").get()
            img_link = product.xpath(".//preceding::div[@class='product-img-outer']/a/img[1]/@data-src").get()

            yield {
                'Name': name,
                'URL' : url,
                'Price': price,
                'Image': img_link
            }

        next_page = response.xpath("//ul[@class='pagination']/li[last()]/a[@rel='next']/@href").get()
        if next_page:
            yield scrapy.Request( url = next_page , callback=self.parse )