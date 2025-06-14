import scrapy
from

class ShellsSpider(scrapy.Spider):
    name = "shells"
    allowed_domains = ["www.bspider.top"]
    start_urls = ["http://www.bspider.top/fangke/"]

    def parse(self, response):
        pass
