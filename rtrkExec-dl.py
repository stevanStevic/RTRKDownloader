import scrapy
import urllib
import os

class ExercisesSpider(scrapy.Spider):
    name = "exercisesSpider"

    def start_requests(self):
        if not hasattr(self, 'link'):
            print "[usage] scrapy runspider rtrkExec-dl.py -a link=http://example.com -a dir=/path/to/dir"
        else:
            yield scrapy.Request(self.link)

    def parse(self, response):
        if hasattr(self, 'dir'):
            os.chdir(self.dir)

        for exerciseUrl, exerciseName in zip(response.css('div#laboratorijske a::attr(href)').extract(), response.css('div#laboratorijske a p::text').extract()):
            exerciseName = exerciseName.strip()
            urllib.urlretrieve(exerciseUrl, exerciseName)