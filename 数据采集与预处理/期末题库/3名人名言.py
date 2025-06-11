#3.爬取1-3页的名人名言页面，获取名人名言和作者两项信息，
# 网址https://quotes.toscrape.com，
# 结果存放到“名人名言.csv”文件，保存在datas目录，如果目录不存在，先创建目录。
import requests
from lxml import etree
import csv
import os
# 确保datas目录存在
# 如果不存在则会自动创建
os.makedirs('datas', exist_ok=True)
def get_html(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None
def parse(html):
    doc = etree.HTML(html)
    out_list = []
    for row in doc.xpath('//div[@class="quote"]'):
        # 名言内容
        quote = row.xpath('.//span[@class="text"]/text()')[0].strip()
        # 作者
        author = row.xpath('.//small[@class="author"]/text()')[0].strip()

        out_list.append([quote, author])
    return out_list

if __name__=="__main__":
    start_url="https://quotes.toscrape.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    csv_file = '名人名言.csv'
    fieldnames = ['quote', 'author']  # CSV 文件的表头

    # 创建 CSV 文件并写入表头
    with open('./datas/'+csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    for i in range(1,4):
        if i==1:
            url= start_url
        else:
            url = f"{start_url}/page/{i}"
        html = get_html(url, headers)
        # 解析数据
        data=parse(html)
        print(f"第{i}页数据解析成功，共获取{len(data)}条数据")
        # 写入CSV文件
        with open('./datas/'+csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
