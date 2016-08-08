# -*- coding: utf8 -*-

from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from yangshengtang.items import Topic
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

import itertools


class YangShTSpider(BaseSpider):
    name = "yangshengtang"
    allowed_domains = ['com']


    def start_requests(self):
        d = {
            '201412': ["http://yangshengtang123.com/yangshengtang/list_68.html",
                       "http://yangshengtang123.com/yangshengtang/list_82_2.html",
                       "http://yangshengtang123.com/yangshengtang/list_82_1.html"
                ]
            }
        for cate, urls in d.iteritems():
            for url in urls:
                yield Request(url=url, dont_filter=True, callback=self.parse_month_list, meta={"cate": cate})

    def parse_month_list(self, response):
        sel = Selector(response)

        for link in sel.xpath('//h2[@class="list_news_tit"]/a/@href').extract():
            yield Request(url=link, callback=self.parse_view_topic, meta=response.meta)

    def parse_view_topic(self, response):
        sel = Selector(response)
        item = Topic()
        title = sel.xpath('//div[@class="xiaomi"]/text()').extract()
        view_url = sel.xpath('//div[@class="viewbox"]//p/strong/a/@href').extract()
        item['title'] = ''.join(title).replace(',', '')
        url_tmp = []
        for url in view_url:
            if url.endswith('.mp4'):
                url_tmp.append(url)
        item['view_url'] = ','.join(url_tmp)

        yield item

