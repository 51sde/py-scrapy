#-*-coding:utf-8-*-

import scrapy
import gzip


class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["ip138.com"]
    start_urls = [
        "http://www.ip138.com:8080/search.asp?action=mobile&mobile=18701760000"
    ]

    def parse(self, response):
        for c in response.xpath('//td[@class="tdc2"]'):
            data = c.xpath("text()").extract()
            print data[0]