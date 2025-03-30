import requests
from lxml import etree

def get_html(url, time=10):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        r = requests.get(url, headers=headers, timeout=time)
        r.raise_for_status()  # 检查请求是否成功
        r.encoding = r.apparent_encoding  # 设置编码
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"请求错误：{e}")
        return None

def parse_news(html):
    if not html:
        return []

    tree = etree.HTML(html)
    news_list = []

    # 获取所有新闻元素
    news_items = tree.xpath('//div[@class="hotnews"]//a')

    for news in news_items:
        title = news.xpath('string(.)')  # 获取所有文本内容
        if title.strip():
            news_list.append({
                'title': title.strip()
            })
    other_news = tree.xpath('//ul[@class="ulist focuslistnews"]//a')
    for news in other_news:
        # 合并每条文本
        title = news.xpath('string(.)')  # 用于获取当前节点和所有子节点的文本内容
        if title.strip():
            news_list.append({
                'title': title.strip()
            })

    return news_list
def save_news(news_list):
    with open('news.txt', 'w', encoding='utf-8') as f:
        for news in news_list:
            f.write(f"{news['title']}\n")
if __name__ == '__main__':
    url = 'https://news.baidu.com/'
    html = get_html(url)
    res_list = parse_news(html)
    save_news(res_list)
    for news in res_list:
        print(f"{news['title']}")