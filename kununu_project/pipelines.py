import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):

    def process_item(self, item, spider):
        item['rating'] = item['rating'].strip()
        item['rating'] = float(item['rating'].replace(',', "."))
        print("pipeline: {} ".format(item['rating']))
        return item
