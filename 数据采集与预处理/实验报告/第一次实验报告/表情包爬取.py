import requests
import re


def get_img(r, name):
    with open('./img/'+name + '.gif','wb+') as f:
        f.write(r.content)


def save_img(url,headers):
    r = requests.get(url=url,headers=headers)
    return r


def get_name(url):
    match = re.search(r'/([^/.]+)\.[^/]+$', url)  # 正则表达式
    return match.group(1)


url_list = ['http://www.bspider.top/static/yh31/images/201910091428546196.gif',
            'http://www.bspider.top/static/yh31/images/202002111326013132.gif',
            'http://www.bspider.top/static/yh31/images/201904090036203114.gif',
            'http://www.bspider.top/static/yh31/images/202011211718017134.gif']
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
for url in url_list:
    r = save_img(url,headers)
    name = get_name(url)
    get_img(r, name)
