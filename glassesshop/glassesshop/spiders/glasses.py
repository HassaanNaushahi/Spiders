# -*- coding: utf-8 -*-
import scrapy

class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath('//div[@id="product-lists"]/div[@class ="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]')
        
        for product in products:
            name = product.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[@class="col-6 col-lg-6"]/div[@class="p-title"]/a[@title]/text()').get()
            name = name.strip()
            link = product.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[@class="col-6 col-lg-6"]/div[@class="p-title"]/a/@href').get()
            price = product.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[@class="col-6 col-lg-6"]/div[@class="p-price"]/div/span/text()').get()
            yield{
                'name': name,
                'link': link, 
                'price': price
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()

        if next_page is not None:
            yield scrapy.Request(url=next_page, callback=self.parse)
        
