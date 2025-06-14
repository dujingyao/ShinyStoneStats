# 爬取1-3页的工学院就业信息网的“招聘单位”和“浏览人数”这两项数据，
# 网址https://hngxy.goworkla.cn/module/position_brief/nid-5598，
# 结果存放到“就业信息.csv”，保存在datas目录中，如果目录不存在，先创建目录。
import requests
import os
import csv
from lxml import etree
os.makedirs("datas", exist_ok=True)

def get_html(url,headers):
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text

def parse(html):
    doc=etree.HTML(html)
    # 在该函数里接收数据的列表
    out_list=[]
    for row in doc.xpath('//div[@class="infoTips"]'):
        name=row.xpath('.//p[@class="tipName"]/text()')
        number=row.xpath('.//p[@class="tipTime" and contains(text(),"浏览人数")]/text()')
        out_list.append({"name":name,"number":number})
    return out_list

if __name__=="__main__":
    start_url="https://hngxy.goworkla.cn/module/position_brief/nid-5598"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 准备 CSV 文件
    csv_file='就业信息.csv'
    fieldnames=['name','number']  # CSV 文件的表头
    # 创建 CSV 文件并写入表头
    with open('./datas/'+csv_file,'w',newline="",encoding="utf-8") as f:
        # 创建 CSV 写入器
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        # 写入表头
        writer.writeheader()
    for i in range(1,4):
        if i==1:
            url=start_url
        else:
            url=f"{start_url}/page-{i}"
        html=get_html(url,headers)
        # if i==1:
        #     print(html)
        # 解析数据
        # 接收的信心应该是一个列表
        datas=parse(html)
        # if i==1:
        #     print(datas)
        # 写入csv文件
        with open("./datas/"+csv_file,'a',newline="",encoding="utf-8") as f:
           writer=csv.DictWriter(f,fieldnames=fieldnames)
              # 写入数据
           for data in datas:
               writer.writerow(data)