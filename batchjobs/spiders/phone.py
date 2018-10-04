# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PhoneSpider(CrawlSpider):
    name = 'phone'
    allowed_domains = ['www.receivesms.co']
    start_urls = ['https://www.receivesms.co/active-numbers/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        i = {}
        # print response
        # self.logger.error('=== === == = == = = =Parse function called on %s', response.text())
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        for sel in response.css('tbody tr'):
            country = sel.xpath('td[2]/a/text()').extract()
            phone = sel.xpath('td[3]/a/text()').extract()
            added = sel.xpath('td[4]/text()').extract()
            detailUrl = sel.xpath('td[5]/a/@href').extract()
            self.logger.info('C: %s, P: %s, A: %s, D: %s', country, phone, added, detailUrl)
        return i
