#3.爬取1-3页的名人名言页面，获取名人名言和作者两项信息，
# 网址https://quotes.toscrape.com，
# 结果存放到“名人名言.csv”文件，保存在datas目录，如果目录不存在，先创建目录

import os

os.makedirs("datas",exist_ok=True)

# /page/2/

if __name__=="__main__":
    start_url="https://quotes.toscrape.com"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 准备 CSV 文件
    csv_file='名人名言.csv'