import urllib.request
import urllib.parse

url = 'https://www.baidu.com?wd='

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# 将周杰伦的名字变成unicode编码的方式

name = urllib.parse.quote('周杰伦')

url = url + name

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read.decode('utf-8')

print(content)
