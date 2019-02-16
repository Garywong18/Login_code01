# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
# 将settings里面的UserAgent_List导入
from Login_code01.settings import UserAgent_List
class RandomUserAgentMiddlewares():
    # user-agent可以直接写在这里，也可以放到settings.py里面
    # UserAgent_List = [
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/536.36',
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/538.36',
    #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/539.36'
    # ]
    def process_request(self,request,spider):
        # 随机User-Agent
        random_useragent = random.choice(UserAgent_List)
        # 设置请求头
        request.headers['User-Agent'] = random_useragent

      # 验证User-Agent是否生效
class ChickUserAgent():
    def process_response(self,request,response,spider):
        useragent = request.headers['User-Agent']
        print(useragent)
        return response

# 设置代理
class ProxyMiddlewares():
    def process_request(self,request,spider):
        request.meta['proxy'] = 'http://188.188.188.88:8080'