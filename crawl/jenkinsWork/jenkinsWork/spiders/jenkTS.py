# << Swami Shreeji >> 
# @nishantpatel ; 10 Oct 2017
# To run from shell --> scrapy crawl jenkTS -a filename=test.txt 
	# where test.txt is the plugins file with associated URLs

import sys
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "jenkTS"
   
    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):
        yield {
        	'plugID': response.css('.sub+ .sub::text').extract(),
        	'dependency': response.css('div.required a::text').extract(),
        }