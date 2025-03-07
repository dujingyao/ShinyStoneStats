import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# url代表的是下载的路径 filename代表的是文件的名字
# 在py中，可以写变量的名字，也可以直接写值
urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片


# 下载视频