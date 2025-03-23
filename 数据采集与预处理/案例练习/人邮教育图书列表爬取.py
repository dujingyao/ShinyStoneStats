# https://www.ryjiaoyu.com/book
# https://www.ryjiaoyu.com/book?tab=book&sort=new&mode=List&page=1
# https://www.ryjiaoyu.com/book?tab=book&sort=new&mode=List&page=2
# 导入库
import time
import requests
import os
import csv
import re,json

from urllib3.filepost import writer


def get_html(url,time=10):
    try:
        headers={
            'ues-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
        }
        # 1.模拟浏览器向服务器发送请求
        res=requests.get(url,headers=headers)
        res.raise_for_status()
        res.encoding=res.apparent_encoding
        return res
    except Exception as err:
        print(err)  # 打印错误数据
#解析
# def parse_html(res):
#     #  <a href="/book/details/52661" title="消费者心理与行为（附微课 第2版）">
#     #  <a href="/book/details/49005" title="经济法基础（微课版）">
#     books=re.search(r'<a href="/book/details/.*？" title="(.*?)">',res.text,re.S).group(1)
#     out_list=[]
#     for book in books:
#         out_list.append(book)
#     return out_list
def parse_html(res):
    # 完整的a标签匹配模式
    # 只能获取一个
    # books = re.search(r'<a href="/book/details/\d+".*?title="(.*?)">', res.text, re.S).group(1)
    # 应该用finder，可以获取多个数据
    pattern= r'<a href="/book/details/\d+" title="(.*?)">'
    books=re.finditer(pattern,res.text,re.S)
    out_list=[]
    for book in books:
        title=book.group(1)
        # print(title)
        out_list.append(title)
    return out_list

def save_data(data):
    with open('books.csv','a', newline="", encoding="utf-8") as f:
        # writer=csv.writer(f)
        # writer.writerow(['书名'])  # 写入表头
        writer = csv.writer(f)
        # 将字符串包装成列表，作为一行写入csv文件
        writer.writerow([data])
if __name__=='__main__':
    url='https://www.ryjiaoyu.com/book'
    # # os是操作系统模块，获取当前工作目录
    # current_dir = os.getcwd()
    # # path是一个路径，确保数据文件blog.csv保存在datas子目录下
    # path = current_dir + "\\datas\\"

    html=get_html(url)
    book_list = parse_html(html)
    for book in book_list:
        save_data(book)
    for page in range(1,5):
        html=get_html(url+r'?tab=book&sort=new&mode=List&page={}'.format(page))
        if html:
            book_list=parse_html(html)
            if book_list:
                for book in book_list:
                    save_data(book)

        time.sleep(1)
    # print(html.text)
    # print(book_list)