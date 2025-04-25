import scrapy
from scrapy import cmdline
from house.items import ShellsItem
import re
class ShellsSpider(scrapy.Spider):
    name = "shells"
    allowed_domains = ["www.bspider.top/fangke"]
    start_urls = ["http://www.bspider.top/fangke/pg"+str(i) for i in range(1,11)]

    def parse(self, response):
        # print(response.text)
        for row in response.xpath('//ul[@class="resblock-list-wrapper"]/li'):
            item=ShellsItem()
            item["house"]=row.xpath('div/div[1]/a/text()').get().strip()
            item["address"]=row.xpath('div/a[1]/@title').get().strip()
            price=row.xpath('string(.div/div[4]/div[1])').get().strip()
            item["price"]=re.sub("\\s+","",price) # 去除空格
            total=row.xpath('div/div[4]/div[2]/text()').get().strip()
            total=total.replace("总价","") if total is not None else ""
            item["total"]=total
            yield item

if __name__ == '__main__':
    cmdline.execute("scrapy crawl shells -o b2.csv".split())