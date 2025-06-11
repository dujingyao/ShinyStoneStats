#4.爬取古诗文网唐诗三百首页面，获取“诗词名称”、“作者”和“诗词正文”三项信息，
# 网址http://www.bspider.top/gushiwen/ts，
# 结果存放到“唐诗三百首.csv”文件，保存在datas目录，如果目录不存在，先创建目录。
# 爬取速度较慢
import requests
from lxml import etree
import csv
import os
# 确保datas目录存在
# 如果不存在则会自动创建
os.makedirs('datas', exist_ok=True)

def get_html(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None

def parse(html, base_url, headers):
    doc = etree.HTML(html)
    out_list = []
    for row in doc.xpath('//div[@class="typecont"]/span'):
        # 获取诗名
        poem_name_list = row.xpath('./a/text()')
        poem_name = poem_name_list[0] if poem_name_list else "未知诗名"

        # 获取作者
        author_list = row.xpath('./text()')
        author = author_list[0].strip("()") if author_list else "未知作者"

        # 获取诗的内容链接
        poem_href_list = row.xpath('./a/@href')
        poem_href = poem_href_list[0] if poem_href_list else None

        if poem_href:
            poem_url = base_url + poem_href
            # print(f"正在获取诗句页面: {poem_url}")
            poem_html = get_html(poem_url, headers)
            if poem_html:
                poem_doc = etree.HTML(poem_html)
                # 获取诗句内容
                poem_content_list = poem_doc.xpath('//div[@class="contson"]//text()')
                poem_content = "".join(poem_content_list).strip().replace('\n', '')
            else:
                poem_content = "获取失败"
        else:
            poem_content = "链接不存在"

        out_list.append({
            'poem_name': poem_name,
            'author': author,
            'poem_content': poem_content
        })
    return out_list

if __name__ == "__main__":
    base_url = "http://www.bspider.top"
    url = f"{base_url}/gushiwen/ts"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # 准备CSV文件
    csv_file = '唐诗三百首.csv'
    fieldnames = ['poem_name', 'author', 'poem_content']

    # 创建CSV文件并写入表头
    with open('./datas/'+csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    html = get_html(url, headers)
    if html:
        poems = parse(html, base_url, headers)
        print(f"数据解析成功，共获取{len(poems)}首诗")

        # 将数据写入CSV文件
        with open('./datas/'+csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for poem in poems:
                writer.writerow(poem)

        print(f"数据已保存到 {csv_file}")