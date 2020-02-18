# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class XijiProxyPipeline(object):
    def __init__(self):
        self.fp=open("ip.json","w")
    def open_spider(self,spider):
        print "hello world"

    def process_item(self, item, spider):
        item_json=json.dumps(dict(item),ensure_ascii=False)#item不能直接转换成json，我们先将其转换成字典再dumps
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self,spider):
        self.fp.close()
        print "end spider"