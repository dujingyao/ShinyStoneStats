import urllib.request
import urllib.parse

# 请求路径
url = 'https://fanyi.baidu.com/sug'
# 请求参数
data = {
    'kw':'spider'
}
# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# post请求的参数，必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数 是不会拼接在url后面的 而是需要放在请求对象定制的参数中
# post请求的参数 必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

# print(content)

# 字符串-->json对象
import json
obj = json.loads(content)
print(obj)
