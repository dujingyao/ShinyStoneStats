# 爬取1-3页的工学院就业信息网的“招聘单位”和“浏览人数”这两项数据，
# 网址https://hngxy.goworkla.cn/module/position_brief/nid-5598，
# 结果存放到“就业信息.csv”，保存在datas目录中，如果目录不存在，先创建目录。

import requests
from lxml import etree
import csv
import os


def get_html(url, headers):
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


if __name__ == "__main__":
    for i in range(1, 4):
        url = f"https://hngxy.goworkla.cn/module/position_brief/nid-5598/page-{i}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        html = get_html(url, headers)
        print(html)
