import requests
from lxml import etree
import time
import re


def get_html(url, retry_times=3, timeout=10):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

    for i in range(retry_times):
        try:
            # 向服务器发送请求
            r = requests.get(url, headers=headers, timeout=timeout)
            # 检查响应状态码
            r.raise_for_status()
            # 设置编码格式
            r.encoding = r.apparent_encoding
            return r.text
        except requests.RequestException as e:
            print(f"第{i + 1}次请求失败：{e}")
            if i < retry_times - 1:
                time.sleep(2)  # 请求失败后等待2秒再重试
                continue
            else:
                print("达到最大重试次数，请求失败")
                return None



def parse_news(html):
    """解析新闻内容"""
    if not html:
        return []

    try:
        # 使用lxml解析HTML
        tree = etree.HTML(html)
        # 获取新闻内容
        news_items = []

        # 获取热点要闻
        hot_news = tree.xpath('//div[@class="hotnews"]//a')
        for news in hot_news:
            # 处理每条新闻
            # 合并每条文本
            title = news.xpath('string(.)')
            if title:
                news_items.append({
                    'title': title,
                    'type': '热点要闻'
                })

        # 获取其他新闻
        other_news = tree.xpath('//ul[@class="ulist focuslistnews"]//a')
        for news in other_news:
            # 合并每条文本
            title = news.xpath('string(.)') # 用于获取当前节点和所有子节点的文本内容
            if title:
                news_items.append({
                    'title': title,
                    'type': '一般新闻'
                })

        return news_items

    except Exception as e:
        print(f"解析错误：{e}")
        return []

def save_news(news_list, filename='news.txt'):
    """保存新闻到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for idx, news in enumerate(news_list, 1):
                f.write(f"[{idx}] {news['type']}\n")
                f.write(f"标题：{news['title']}\n")
                f.write('-' * 50 + '\n')
    except IOError as e:
        print(f"保存文件失败：{e}")


def main():
    url = 'https://news.baidu.com/'
    print("开始获取新闻...")

    # 获取页面内容
    html = get_html(url)
    if not html:
        print("获取页面失败")
        return

    # 解析新闻
    news_list = parse_news(html)
    if not news_list:
        print("未获取到新闻")
        return

    # 打印结果
    print(f"\n共获取到 {len(news_list)} 条新闻：")
    for idx, news in enumerate(news_list, 1):
        print(f"\n[{idx}] {news['type']}")
        print(f"标题：{news['title']}")

    # 保存到文件
    save_news(news_list)
    print(f"\n新闻已保存到 news.txt")


if __name__ == '__main__':
    main()