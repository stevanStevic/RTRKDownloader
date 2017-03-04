import scrapy
import urllib
import os

class LecturesSpider(scrapy.Spider):
    name = "lecturesSpider"

    def start_requests(self):
        if not hasattr(self, 'link'):
            print "[usage] scrapy runspider rtrkLec-dl.py -a link=http://example.com -a dir=/path/to/dir"
        else:
            yield scrapy.Request(self.link)

    def parse(self, response):
        if hasattr(self, 'dir'):
            os.chdir(self.dir)

        for lectureUrl, lectureName in zip(response.css('div#predavanja a::attr(href)').extract(), response.css('div#predavanja a p::text').extract()):
            lectureName = lectureName.strip()
            urllib.urlretrieve(lectureUrl, lectureName)