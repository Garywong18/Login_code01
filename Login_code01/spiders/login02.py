# -*- coding: utf-8 -*-
import scrapy
# 通过发送Data来登陆

class Login02Spider(scrapy.Spider):
    name = 'login02'
    allowed_domains = ['yaozh.com']
    start_urls = ['https://www.yaozh.com/login/']

    # 携带参数登陆成功获取cookies
    def parse(self, response):
        login_url = 'https://www.yaozh.com/login'
        formhash = response.xpath("//input[@id='formhash']/@value").extract_first()
        backurl = response.xpath("//input[@id='backurl']/@value").extract_first()
        FormData = {
            'username':'xxx',
            'pwd':'xxx',
            'formhash':formhash,
            'backurl':backurl
        }
        yield scrapy.FormRequest(
            login_url,
            formdata=FormData,
            callback=self.parse_login
        )
    # 携带cookies继续请求目标页面
    def parse_login(self,response):
        member_url = 'https://www.yaozh.com/member/'
        yield scrapy.Request(
            member_url,
            callback=self.parse_member
        )
    # 解析目标页面
    def parse_member(self,response):
        item = {}
        item['user_name'] = response.xpath('//h1[@class="Y_Yahei Y_f14"]/a/text()').extract_first()
        item['account'] = response.xpath('//em[@class="Y_Yahei Y_f32"]/label/text()').extract_first()
        print(item['user_name'])
        print(item['account'])