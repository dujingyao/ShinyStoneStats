import urllib.request

url = 'https://ssr1.scrape.center/page/3'
# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 解析网络源码
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据  xpath的返回值是一个列表类型的数据
result_name = tree.xpath('//div[@class="el-col el-col-18 el-col-offset-3"]//a//h2/text()')
score = tree.xpath('//div[@class="el-col el-col-18 el-col-offset-3"]//div//p/text()')
time = tree.xpath('//div[@class="el-col el-col-18 el-col-offset-3"]//div//span/text()')
print(f'{result_name[0]}')
print(f'{time[0]} {time[1]} {time[2]} {time[4]}')
print(f'{score[0]}')
with open('movie.txt', 'w', encoding ='utf-8') as f:
    f.write(f'{result_name[0]}')
    f.write('\n')
    f.write(f'{time[0]} {time[1]} {time[2]} {time[4]}')
    f.write('\n')
    f.write(f'{score[0]}')

