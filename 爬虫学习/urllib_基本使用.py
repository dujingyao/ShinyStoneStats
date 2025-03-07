# 使用urllib获取百度的源码
import urllib.request

# 1. 定义一个url 就是要访问的网址
url = 'http://www.baidu.com'

# 2. 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3. 获取响应中的页面的源码
# read方法，返回的是字节形式的二进制文件
# 将二进制转换为字符串 解码 decode
content = response.read().decode('utf-8')

# 4. 打印数据
print(content)