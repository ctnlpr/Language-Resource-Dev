import scrapy
import codecs
from scrapy.selector import Selector


class Tutorial1Spider(scrapy.Spider):
    name = "thinakaran2"
    allowed_domains = ['thinakaran.lk']
    start_urls = [
        'http://www.thinakaran.lk/',
    ]

    def start_requests(self):
        count = 0  # to 387
        while count < 4:
            request = scrapy.Request('http://www.thinakaran.lk/?page=Technology' + str(count), callback=self.parse_request)
            yield request
            count += 1

    def parse_request(self, response):
        links = response.xpath('//div[@class="views-field views-field-title"]/span/a/@href').extract()
        i = 6
        while i < 16:
            yield scrapy.Request('http://www.thinakaran.lk' + links[i], callback=self.parse)
            i += 1

    def parse(self, response):
        heading = response.xpath('//h1[@id="page-title"]/text()').extract_first()
        date = response.xpath('//span[@class="date-display-single"]/@content').extract_first().split('T')[0]
        id = response.url.split('/')[-1]
        some = response.xpath('//div[@property="content:encoded"]/p').extract()
        htmltag = "p"
        if not some:
            some = response.xpath('//div[@property="content:encoded"]/div').extract()
            htmltag = "div"
        content = ''
        for s in some:
            content += Selector(text=s).xpath('string(//' + htmltag + ')').extract_first()
        yield {
            'id':id,
            'heading':heading,
            'content':content,
            'date':date,
            'url': response.url,
            'tag': 'Technology'
        }
