#-*-coding:utf-8-*-

import scrapy
from scrapy.http import Request

class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["ip138.com"]
    start_urls = [
        "http://localhost"
    ]

    format_url = "http://www.ip138.com:8080/search.asp?action=mobile&mobile={mobile}"

    def parse(self, response):
        mobiles = [
            "1870176",
            "1380539",
            "1718538",
        ]

        for mobile in mobiles:
            url = self.format_url.replace("{mobile}", mobile)

            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        for c in response.xpath('//td[@class="tdc2"]').xpath("text()"):
            data = c.extract()
            print data


