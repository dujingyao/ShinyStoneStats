import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
# 接受回应数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 下载到本地
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
