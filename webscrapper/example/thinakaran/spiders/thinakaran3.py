import scrapy
import codecs
from scrapy.selector import Selector

class Tutorial1Spider(scrapy.Spider):
    name = "thinakaran3"
    allowed_domains = ['thinakaran.lk']
    start_urls = [
        'http://www.thinakaran.lk/2017/05/19/%E0%AE%89%E0%AE%B3%E0%AF%8D%E0%AE%A8%E0%AE%BE%E0%AE%9F%E0%AF%81/17729',
    ]

    # def start_requests(self):
    #     count = 20025
    #     while count < 20045:
    #         request = scrapy.Request('http://www.virakesari.lk/article/' + str(count), callback=self.parse)
    #         request.meta['id'] = count
    #         yield request
    #         count += 1

    def parse(self, response):
        some = response.xpath('//div[@property="content:encoded"]/p').extract()
        htmltag="p"
        if not some:
            some = response.xpath('//div[@property="content:encoded"]/div').extract()
            htmltag="div"
        content = ''
        for s in some:
            content += Selector(text=s).xpath('string(//'+htmltag+')').extract_first()
        print content
