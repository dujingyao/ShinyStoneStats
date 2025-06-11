# 爬取1-3页的工学院就业信息网的“招聘单位”和“浏览人数”这两项数据，
# 网址https://hngxy.goworkla.cn/module/position_brief/nid-5598，
# 结果存放到“就业信息.csv”，保存在datas目录中，如果目录不存在，先创建目录。
import requests
from lxml import etree
import csv
import os
# 确保datas目录存在
# 如果不存在则会自动创建
os.makedirs('datas', exist_ok=True)
def get_html(url, header):
    """获取网页内容"""
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = response.apparent_encoding  # 设置编码格式
        return response.text
    except requests.RequestException as e:
        print(f"请求错误：{e}")
        return None

def parse(html):
    doc = etree.HTML(html)
    out_list = []
    for row in doc.xpath('//div[@class="infoTips"]'):
        # 获取招聘单位
        name= row.xpath('.//p[@class="tipPlace"]/text()')
        # 获取浏览人数
        number= row.xpath('.//p[@class="tipTime" and contains(text(), "浏览人数")]/text()')

        out_list.append({
            'name': name,
            'number': number
        })
    return out_list

if __name__ == "__main__":
    start = "https://hngxy.goworkla.cn/module/position_brief/nid-5598"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    csv_file = '就业信息.csv'
    fieldnames = ['name', 'number'] # CSV 文件的表头

    # 创建 CSV 文件并写入表头
    with open('./datas/'+csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    # 爬取数据并写入 CSV 文件
    for i in range(1, 4):
        if i == 1:
            url = start
        else:
            url = f"{start}/page-{i}"
        html = get_html(url, headers)
        if html:
            print(f"第{i}页内容获取成功")
            data = parse(html)
            print(f"第{i}页数据解析成功，共获取{len(data)}条数据")
            with open('./datas/'+csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerows(data)
        else:
            print(f"第{i}页内容获取失败")