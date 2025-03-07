# 请求对象定制
# 获取响应的数据
# 下载数据
import urllib.parse
import urllib.request


def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码：'))
    end_page = int(input('请输入结束的页码：'))

    for page in range(start_page, end_page + 1):    #         每一页都要有自己的请求对象的请求
        request = creat_request(page)
        content = get_content(request)
        down_load(page, content)
