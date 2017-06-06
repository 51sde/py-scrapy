#-*-coding:utf-8-*-

import scrapy


class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["ip138.com"]
    start_urls = [
        "http://www.ip138.com:8080/search.asp?action=mobile&mobile=18701766310"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        print '你好，世界'
        with open(filename, 'wb') as f:
            f.write(response.body)

