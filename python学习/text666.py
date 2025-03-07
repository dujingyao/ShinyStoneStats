# 使用requests爬取豆瓣电影Top250，结果保存为JSON
import requests
import re
import json
from bs4 import BeautifulSoup
def get_html(url,time=10):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    try:
        r=requests.get(url,headers=headers,timeout=time)
        r.encoding=r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as error:
        print(error)
def get_info(html):
    soup=BeautifulSoup(html,'html.parser')
    movies=soup.find_all('div',class_='item')
    for movie in movies:
        title=movie.find('span',class_='title').string
        score=movie.find('span',class_='rating_num').string
        yield {
            'title':title,
            'score':score
        }
def save_json(data):
    with open('douban.json','w',encoding='utf-8') as f:
        f.write(json.dumps(data,ensure_ascii=False))
if __name__=='__main__':
    url='https://movie.douban.com/top250'
    html=get_html(url)
    data=[]
    for item in get_info(html):
        data.append(item)
    save_json(data)
    print('保存成功')
# Compare this snippet from 数据采集与预处理/实验报告/第一次实验报告/手机号归属地查询.py:

