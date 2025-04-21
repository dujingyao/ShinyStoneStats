import scrapy
from scrapy import cmdline
from baiduspider.items import BaiduspiderItem

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        # print(response.text)
        alist = response.xpath('//div[@id="u1"]/a')
        # print(alist)
        for row in alist:
            item = BaiduspiderItem()
            txt = row.xpath("text()")
            href = row.xpath("@href")
        # alist = response.css('div#s-top-left > a')  # 使用CSS等价于原 XPath
        # for row in alist:
        #     item = BaiduspiderItem()
        #     txt = row.css('::text')  # 提取文本
        #     href = row.css('::attr(href)')  # 提取 href 属性

            if txt:
                print(txt.get().strip())
                print(href.get().strip())
                item["title"] = txt.get().strip()
                item["url"] = href.get().strip()
                yield item

if __name__ == '__main__':
    cmdline.execute("scrapy crawl baidu".split())