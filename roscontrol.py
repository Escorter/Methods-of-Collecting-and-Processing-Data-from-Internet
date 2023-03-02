# Паук 'roscontrol' парсит сайт roscontrol.com,
# собирает информацию о продуктах в файл products.csv,
# а также загружает ее в БД 'products'

import scrapy
from pymongo import MongoClient


class BookSpider(scrapy.Spider):
    name = "roscontrol"
    allowed_domains = ["roscontrol.com"]
    start_urls = ["https://roscontrol.com/category/produkti/ptitsa-1/file/"]

    def parse(self, response):
        print('*******************************************************')
        goods = response.css("li.product")
        client = MongoClient()
        db = client['products']
        collection = db['chicken']
        for item in goods:
            row = {
                'title': item.css(
                    "h2.woocommerce-loop-product__title::text").get(),
                'brand': item.css("p.brand-text::text").get(),
                'value': item.css("span.num::text").getall()[0],
                'natural': item.css("span.num::text").getall()[1],
                'safety': item.css("span.num::text").getall()[2],
                'quality': item.css("span.num::text").getall()[3],
                'link': item.css(
                    "a.woocommerce-LoopProduct-link::attr('href')").get()
            }
            collection.insert_one(row)
            yield row
