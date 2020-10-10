import scrapy
import codecs


class Tutorial1Spider(scrapy.Spider):
    name = "thinakaran"
    allowed_domains = ['thinakaran.lk']
    start_urls = [
        'http://www.thinakaran.lk/political?page=1',
    ]

    # def start_requests(self):
    #     count = 20025
    #     while count < 20045:
    #         request = scrapy.Request('http://www.virakesari.lk/article/' + str(count), callback=self.parse)
    #         request.meta['id'] = count
    #         yield request
    #         count += 1

    def parse(self, response):
        links = response.xpath('//div[@class="views-field views-field-title"]/span/a/@href').extract()
        for s in links:
            print s
            print "hello"
