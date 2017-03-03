import scrapy
import urllib

class LecturesSpider(scrapy.Spider):
    name = "lecturesSpider"

    def start_requests(self):
        #link = getattr(self, 'link', None)
        #if link is None:
        #    print "[usage] scrapy runspider rtrk-dl.py link=http://example.com"
        #    exit()
        yield scrapy.Request(self.link)

    def parse(self, response):
        for lectureUrl, lectureName in zip(response.css('div#predavanja a::attr(href)').extract(), response.css('div#predavanja a p::text').extract()):
            lectureName = lectureName.strip()
            urllib.urlretrieve(lectureUrl, lectureName)
