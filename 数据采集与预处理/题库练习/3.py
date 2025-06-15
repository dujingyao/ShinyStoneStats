#3.爬取1-3页的名人名言页面，获取名人名言和作者两项信息，
# 网址https://quotes.toscrape.com，
# 结果存放到“名人名言.csv”文件，保存在datas目录，如果目录不存在，先创建目录

import os
import csv
import requests
from lxml import etree
os.makedirs("datas",exist_ok=True)

def get_html(url,headres):
    r=requests.get(url,headers=headres)
    r.raise_for_status()  # 确保请求成功
    r.encoding = r.apparent_encoding  # 设置正确的编码
    return r.text

def parse(html):
    doc=etree.HTML(html)
    out_list = []
    for row in doc.xpath('//div[@class="quote"]'):
        quote=row.xpath('.//span[@class="text"]/text()')[0]
        author=row.xpath('.//small[@class="author"]/text()')[0]
        out_list.append({"quote": quote, "author": author})
    return out_list

# /page/2/

if __name__=="__main__":
    start_url="https://quotes.toscrape.com"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 准备 CSV 文件
    csv_file='名人名言.csv'
    fieldnames=['quote','author']  # CSV 文件的表头
    # 创建 CSV 文件并写入表头
    with open('./datas/'+csv_file,'w',newline='',encoding="utf-8") as f:
        write=csv.DictWriter(f,fieldnames=fieldnames)
        write.writeheader()
    for i in range(1,4):
        if i==1:
            url=start_url
        else:
            url=f"{start_url}/page/{i}"
        html=get_html(url,headers)
        # 解析数据
        datas=parse(html)
        for data in datas:
            with open('./datas/'+csv_file,'a',newline='',encoding="utf-8") as f:
                writer=csv.DictWriter(f,fieldnames=fieldnames)
                writer.writerow(data)
        print(f"第{i}页数据解析成功，共获取{len(datas)}条数据")