#爬取安居客二手房页面，获取“楼房”、“地址”和“单价”三项信息，
# 网址http://www.bspider.top/anjuke，
# 结果存放到“房产信息.csv”文件，保存在datas目录，如果目录不存在，先创建目录。
import requests
from lxml import etree
import csv
import os
# 确保datas目录存在
# 如果不存在则会自动创建
os.makedirs('datas', exist_ok=True)
def get_html(url, headers):
    """
    获取网页源码
    :param url: 网页地址
    :param headers: 请求头
    :return: 网页源码
    """
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

    for row in doc.xpath('//div[@class="property"]'):
        # 楼盘名称
        house = row.xpath("a//*[@class='property-content-info-comm-name']/text()")[0]
        # 地址
        address = row.xpath("string(./a//*[@class='property-content-info-comm-address'])")
        # 价格
        price = row.xpath("a//*[@class='property-price-average']/text()")[0]
        price = price.replace(" ", "")

        row_list = [
            house.strip(),  # 楼盘
            address.strip(),  # 地址
            price  # 房价
        ]
        out_list.append(row_list)

    return out_list

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ '楼盘', '地址', '价格'])
        writer.writerows(data)

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    base_url = 'http://www.bspider.top/anjuke/?page='
    all_data = []  # 用于保存所有页面的数据

    # 爬取第1页到第9页
    for page in range(1, 4):  # 1到3页
        url = base_url + str(page)
        print(f"正在爬取第{page}页: {url}")

        html = get_html(url, headers)
        if not html:
            print(f"获取第{page}页失败，跳过")
            continue

        data = parse(html)  # 修改parse函数只返回数据列表
        all_data.extend(data)
    # 保存数据
    if all_data:
        save_to_csv(all_data, './datas/房产信息.csv')
        print(f"共爬取{len(all_data)}条房源信息")
    else:
        print("未获取到任何数据")