import time

import requests
import os
import csv
import re, json


def get_html(url, time=10):
    # 获得网页内容
    try:
        # 1. 设置请求头模拟浏览器
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
        # 2.向浏览器发送get请求
        # 发送get请求的方法
        # res包含服务器返回的状态码，响应头，响应内容等信息
        # 用于在服务器获取数据
        res = requests.get(url, timeout=time, headers=headers)
        # 3. 检查响应的状态码（4xx/5xx会抛出异常）
        # 检查HTTP响应的状态码
        res.raise_for_status()
        # 4. 设置正确的编码方式防止乱码
        # 自动设置正确的编码方式
        res.encoding = res.apparent_encoding
        # 5. 返回完整的响应对象
        return res
    except Exception as err:
        print(err) # 打印错误数据


def save_data(path, item):
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(item)


def parse_html(res):
    # print(res.text) # 打印出来便于观察我们想要的东西在哪
    # 用正则表达式来获取我们想要的文本
    data = re.search(r'jQuery.*?\((.*?)\);', res.text, re.S).group(1)
    # 将字符串形式的JSON数据解析成字典
    # 解析后从字典中获取键名为"result"的值
    txtresult = json.loads(data)["result"]
    datalist = txtresult["data"]
    ctime = txtresult["end"]
    outlist = []
    for data in datalist:
        title = data["title"]
        author = data["author"]
        summary = data["summary"]

        news = [title, author, summary]
        outlist.append(news)
    result = {"ctime": ctime, "outlist": outlist}
    return result


def run(ctime="", page_limit=3):
    url = f"https://feed.mix.sina.com.cn/api/roll/get?callback=jQuery17206428762630293484_1742464944621&pageid=143&num=30&lid=3108&versionNumber=1.2.8&encode=utf-8&ctime={ctime}&_=1742464945174"
    # 模拟浏览器向服务器发送请求并获取响应数据
    html = get_html(url)
    result = parse_html(html)
    # 获取指定键值对的值
    out_list = result.get("outlist")
    c_time = result.get("ctime")

    if len(out_list) > 0 and page_limit > 0:
        save_data(path + 'blog.csv', out_list)
        print(f"爬取第{3 - page_limit}页")
        time.sleep(3)
        run(c_time, page_limit - 1)


if __name__ == '__main__':
    # os是操作系统模块，获取当前工作目录
    current_dir = os.getcwd()
    # path是一个路径，确保数据文件blog.csv保存在datas子目录下
    path = current_dir + "\\datas\\"
    # 检查目录是否存在
    if not os.path.exists(path):
        os.mkdir(path)
    run()
