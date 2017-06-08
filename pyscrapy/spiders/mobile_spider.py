#-*-coding:utf-8-*-

import scrapy
from scrapy.http import Request

class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["ip138.com"]
    start_urls = [
        "http://localhost"
    ]

    def parse(self, response):
        urls = [
            "http://www.ip138.com:8080/search.asp?action=mobile&mobile=1870176",
            "http://www.ip138.com:8080/search.asp?action=mobile&mobile=1380539",
            "http://www.ip138.com:8080/search.asp?action=mobile&mobile=1718538",
        ]
        for url in urls:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        for c in response.xpath('//td[@class="tdc2"]'):
            data = c.xpath("text()").extract()
            print data[0]

    def a(self):
        pass