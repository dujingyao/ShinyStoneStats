import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# response = urllib.request.urlopen(request)

handler = urllib.request.ProxyHandler

response = urllib.request.build_opener((handler))

content = response.open(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as file:
    file.write(content)