# 请求对象的定制
# 获取网页的源码
# 下载

# 需求 下载前十页的图片
# https://sc.chinaz.com/tupian/xiaomaotupian.html
# https://sc.chinaz.com/tupian/xiaomaotupian_2.html
# https://sc.chinaz.com/tupian/xiaomaotupian_3.html

import urllib.request
from lxml import etree

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/xiaomaotupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/xiaomaotupian_' + str(page) + '.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
#    下载图片   urllib.request.urlretrieve('图片地址','文件的名字')
#     urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//div//div/img/@alt')
#   一般涉及到图片的的网站都会涉及懒加载
    src_list = tree.xpath('//div[@class="container"]//div//div/img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./猫猫图片/'+name+'.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)
