# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['yaozh.com']
    start_urls = ['https://www.yaozh.com/member/']

    def start_requests(self):
        cookies = 'xxxxxxx'
        # cookies字典推导式
        cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split(';')}
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies= cookies
                             )
    def parse(self, response):
        item = {}
        item['user_name'] = response.xpath('//h1[@class="Y_Yahei Y_f14"]/a/text()').extract_first()
        item['account'] = response.xpath('//em[@class="Y_Yahei Y_f32"]/label/text()').extract_first()
        print(item['user_name'])
        print(item['account'])