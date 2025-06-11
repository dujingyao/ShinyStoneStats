# 编写程序，百度图库搜索“人工智能”，
# 获取前两张图片，保存在images目录中。
import requests
import os
# 确保images目录存在
# 如果不存在则会自动创建
os.makedirs('images', exist_ok=True)
url_list=[
    "https://img0.baidu.com/it/u=2958632508,1917305803&fm=253&fmt=auto&app=120&f=JPEG?w=750&h=500",
    "https://img1.baidu.com/it/u=1531338729,2167345062&fm=253&fmt=auto&app=138&f=JPEG?w=688&h=500",
    "https://img2.baidu.com/it/u=2897610453,855795250&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=500"

]
i=0
for url in url_list:
    with open('./images/'+str(i)+'.png','wb+') as f:
        f.write(requests.get(url).content)
    i+=1