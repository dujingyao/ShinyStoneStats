#4.爬取古诗文网唐诗三百首页面，获取“诗词名称”、“作者”和“诗词正文”三项信息，
# 网址http://www.bspider.top/gushiwen/ts，
# 结果存放到“唐诗三百首.csv”文件，保存在datas目录，如果目录不存在，先创建目录。
import csv
import os
import requests
from lxml import etree
os.makedirs("datas", exist_ok=True)

def get_html(url,headers):
    r=requests.get(url=url,headers=headers)
    r.raise_for_status()  # 确保请求成功
    r.encoding = r.apparent_encoding  # 设置正确的编码
    return r.text

def parse(html,headers):
    doc=etree.HTML(html)
    out_list = []
    for row in doc.xpath('//div[@class="typecont"]/span'):
        # 诗名
        poem_name = row.xpath('./a/text()')[0]
        # 作者
        author_list = row.xpath('./text()')
        author = author_list[0].strip("()") if author_list else "未知作者"

        # 诗的内容链接
        poem_href = row.xpath('./a/@href')[0]


        if poem_href:
            poem_url = "http://www.bspider.top" + poem_href
            poem_html = get_html(poem_url, headers)
            if poem_html:
                poem_doc = etree.HTML(poem_html)
                # 诗句内容
                poem_content_list = poem_doc.xpath('//div[@class="contson"]//text()')
                poem_content = "".join(poem_content_list).strip().replace('\n', '')
            else:
                poem_content = "获取失败"
        else:
            poem_content = "链接不存在"

        out_list.append({
            'poem_name': poem_name,
            'author': author,
            'poem_content': poem_content
        })
    return out_list


if __name__=="__main__":
    start_url="http://www.bspider.top/gushiwen/ts"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    csv_file="唐诗三百首.csv"
    # fieldnames 是一个列表，里面的元素是csv的列名
    fieldnames = ['poem_name', 'author', 'poem_content']
    with open('./datas/'+csv_file,'w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
    html=get_html(start_url,headers)
    # 解析数据
    datas=parse(html,headers)
    for data in datas:
        with open('./datas/'+csv_file,'a',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow(data)