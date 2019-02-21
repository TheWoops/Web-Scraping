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

        item['date'] = item['date'].replace('Jan. ', "01.")
        item['date'] = item['date'].replace('Feb. ', "02.")
        item['date'] = item['date'].replace('März', "03.")
        item['date'] = item['date'].replace('Apr. ', "04.")
        item['date'] = item['date'].replace('Mai ', "05.")
        item['date'] = item['date'].replace('Juni ', "06.")
        item['date'] = item['date'].replace('Juli ', "07.")
        item['date'] = item['date'].replace('Aug. ', "08.")
        item['date'] = item['date'].replace('Sep. ', "09.")
        item['date'] = item['date'].replace('Okt. ', "10.")
        item['date'] = item['date'].replace('Nov. ', "11.")
        item['date'] = item['date'].replace('Dez. ', "12.")
        item['date'] = item['date'].replace(' ', "")
        
        return item
