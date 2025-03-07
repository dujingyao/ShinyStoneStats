import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# 按照一个一个字节的读
# content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)
# print(content)

# 按行读
# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)

# 返回状态码 如果是200说明没有错
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取一个状态信息
# print(response.getheaders())
