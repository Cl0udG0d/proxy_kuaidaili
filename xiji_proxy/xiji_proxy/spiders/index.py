# -*- coding: utf-8 -*-
import scrapy
from xiji_proxy.items import XijiProxyItem

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    def parse(self, response):
        iplist=response.xpath('//tr/td[2]/text()').extract()
        portlist=response.xpath('//tr/td[3]/text()').extract()
        typelist=response.xpath('//tr/td[6]/text()').extract()
        for ip,port,proxytype in zip(iplist,portlist,typelist):
            item=XijiProxyItem(proxy_ip=proxytype.lower()+"://"+ip+":"+port)
            yield item
