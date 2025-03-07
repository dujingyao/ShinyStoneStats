import urllib.request

url = 'http://www.baidu.com'

# url的组成
# https://baidu.com/s?wd=周杰伦

# http/https        www.baidu.com     80/443        s       wd=周杰伦   #
#   协议                主机           端口号        路径        参数    锚点
# http      80
# https     443
# mysql     3306
# oracle    1521
# mongodb   27017

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# 因为urlopen方法中不能存放字典，因此headers不能传递进去
# 请求对象的定制
# 注意，因为参数顺序的问题，不能直接写url和headers

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)