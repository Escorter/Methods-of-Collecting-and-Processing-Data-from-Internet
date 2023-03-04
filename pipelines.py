# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from pymongo import MongoClient


class MongoPipeline:
    collection = 'books'

    def open_spider(self, spider):
        self.client = MongoClient()
        self.db = self.client.products

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert_one(ItemAdapter(item).asdict())
        return item
