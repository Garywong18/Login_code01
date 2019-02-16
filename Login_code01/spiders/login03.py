# -*- coding: utf-8 -*-
import scrapy

# 通过scrapy自带的方法来自动解析登陆url与参数
class Login03Spider(scrapy.Spider):
    name = 'login03'
    allowed_domains = ['yaozh.com']
    start_urls = ['https://www.yaozh.com/login/']
    # 携带参数登陆成功获cookie
    def parse(self, response):
        formdata = {
            'username':'xxx',
            'pwd':'xxx'
        }
        yield scrapy.FormRequest.from_response(
            response,
            formid='login_pc', #定位一下需要解析的form
            method='POST', #由于此网站自动解析出来的登陆网址是GET请求，所以需要将method改为POST
            formdata=formdata,
            callback=self.parse_login
        )
    # 携带cookie获取目标页面相应
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