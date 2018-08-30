import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from real_estate.items import RealEstateItem
from real_estate.middlewares import xtract
import json
from scrapy.crawler import CrawlerProcess


class StackSpider(CrawlSpider):
    name = "batdongsan.com"
    allowed_domains = ["batdongsan.com.vn"]
    start_urls = [
        ("https://batdongsan.com.vn/nha-dat-ban/p" + str(page)) for page in range(501, 511)
    ]
    def parse(self, response):
        for href in response.xpath('//*[@id="form1"]/div[4]/div[6]/div[3]/div/div[1]/div[3]/div/div[1]/h3/a/@href').extract():
            yield response.follow(href, self.parse_content)

    def parse_content(self, response):
        item = RealEstateItem()
        item["title"] = xtract(response, '//*[@id="product-detail"]/div[1]/h1/text()')
        item["price"] = xtract(response, '//*[@id="product-detail"]/div[2]/span[2]/span[1]/strong/text()')
        item["area"] = xtract(response, '//*[@id="product-detail"]/div[2]/span[2]/span[2]/strong/text()')
        item['contact'] = xtract(response, '//*[@id="LeftMainContent__productDetail_contactMobile"]/div[2]/text()')
        item['name_contact'] = xtract(response, '//*[@id="LeftMainContent__productDetail_contactName"]/div[2]/text()')
        item['address'] = xtract(response, '//*[@id="product-detail"]/div[8]/div/div[1]/div/div[2]/div[2]/div[2]/text()')
        item['detail'] = xtract(response, '//*[@id="product-detail"]/div[5]/div[1]/text()')
        item['number_bed_room'] = xtract(response, '//*[@id="LeftMainContent__productDetail_roomNumber"]/div[2]/text()')
        yield item
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(batdongsan)
process.start()