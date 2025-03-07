import urllib.request
from lxml import etree

# //div[@class="ggnr"]//div//div//div/div
url = 'http://www.moa.gov.cn/govpublic/SCYJJXXS/202410/t20241025_6465040.htm'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

tree = etree.HTML(content)
works_list = tree.xpath('//div[@class="ggnr"]//div//div//div//div/p/text()')
# '网页文档提取结果.txt'对应上传数据集'2307385106杜净瑶数据科学231_1.txt'
with open('网页文档提取结果.txt', 'w', encoding='utf-8') as file:
    for works in works_list:
            file.write(works)
            file.write('\n')
