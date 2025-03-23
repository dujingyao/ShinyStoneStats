# https://news.baidu.com/widget?id=InternationalNews&t=1742607473460
# https://news.baidu.com/widget?id=EnterNews&t=1742607473468
# https://news.baidu.com/widget?id=FinanceNews&t=1742607473472
# https://news.baidu.com/widget?id=SportNews&t=1742607473476
# https://news.baidu.com/widget?id=TechNews&t=1742611021285
# https://news.baidu.com/widget?id=CarNews&t=1742611021289
# https://news.baidu.com/widget?id=HealthNews&t=1742611021293
# https://news.baidu.com/widget?id=HouseNews&t=1742611021297
# https://news.baidu.com/widget?id=EducationNews&t=1742611021301
# https://news.baidu.com/widget?id=CultureNews&t=1742611021305
# https://news.baidu.com/widget?id=MilitaryNews&t=1742611021309
# https://news.baidu.com/widget?id=LadyNews&t=1742611021359

import  requests
import re
def get_html(url):

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'Cookie': 'select_city=410700; '
                     'lianjia_ssid=bf309382-6328-4ccf-9b4b-6893d0963727; '
                     'lianjia_uuid=56d138e3-877b-4176-9eff-711e993c0c5b; '
                     'Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1742604545; '
                     'HMACCOUNT=661F2DF96ACD0C72; '
                     'sajssdk_2015_cross_new_user=1; '
                     'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195bb549a72bf1-03e259575d9f29-26011d51-929640-195bb549a73884%22%2C%22%24device_id%22%3A%22195bb549a72bf1-03e259575d9f29-26011d51-929640-195bb549a73884%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; '
                     'Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1742604689; '
                     'srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYWVmNGM1MmUyOWZlODg4N2VjYWMzMGFlZDY4MWQ5NjVkNmY1YmMwZWQyZjIzMmQxYzdlZTI4MTliNzAyNmIyMjU3YTFhN2NhNTY4ODQxYTRlOGNlN2E3ZjRlNDU4MzE2NDU2NjQyYTA5NjU2ZTA4ZDdkOGZlOGVmNGQzMjEwYzE2YTE3OTdiNjExODFmZDVjOWUzY2VjYTE3MGYzOTU0ZDBmYzA0YjdhYjFkMjM4MmU5Y2Y3YzY0MTNkY2YwMDMyMjFjYzEwZTgwMzJkZDcxNmZmY2FmNjlkOTk1YWRjZjFmZTZjNmE4NzFkNjNkNDY4OGE0ZmYyM2YxMGRhODdkMDI3ZjhmY2Q0YjA4NzA3OTA0NjI4MGE0Yjg0M2FiMTQwMmI3OGJjNDBiOTY1MjVmYjkxYTIwYTliMWJhMDRmMTBcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiZTFmZDJlZDlcIn0iLCJyIjoiaHR0cHM6Ly94aW54aWFuZy5rZS5jb20vZXJzaG91ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
        }
        # 1.模拟浏览器向服务器发送请求
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res
    except Exception as err:
        print(err)  # 打印错误数据

def parse_html(res):
    patterns = [
        r'<a href="(http[s]?://[^"]+)" mon="[^"]*" target="_blank">(.*?)</a>',
        r'<a href="//(.*?)" mon="[^"]*" target="_blank">(.*?)</a>',
        r'<a href="(.*?)" mon="[^"]*" target="_blank">(.*?)</a>'
    ]
    news_list = []
    for pattern in patterns:
        matches = re.finditer(pattern, res.text, re.S)
        for match in matches:
            if len(match.groups()) == 2:
                url = match.group(1)
                title = match.group(2)
                if 'http' not in url:
                    url = 'http://' + url if '//' in url else 'http://baidu.com' + url
                news_list.append([url, title])

    return news_list


if __name__=='__main__':
    url_list=[
        'https://news.baidu.com/widget?id=InternationalNews&t=1742607473460',
        # 'https://news.baidu.com/widget?id=EnterNews&t=1742607473468',
        # 'https://news.baidu.com/widget?id=FinanceNews&t=1742607473472',
        # 'https://news.baidu.com/widget?id=SportNews&t=1742607473476',
        # 'https://news.baidu.com/widget?id=TechNews&t=1742611021285',
        # 'https://news.baidu.com/widget?id=CarNews&t=1742611021289',
        # 'https://news.baidu.com/widget?id=HealthNews&t=1742611021293',
        # 'https://news.baidu.com/widget?id=HouseNews&t=1742611021297',
        # 'https://news.baidu.com/widget?id=EducationNews&t=1742611021301',
        # 'https://news.baidu.com/widget?id=CultureNews&t=1742611021305',
        # 'https://news.baidu.com/widget?id=MilitaryNews&t=1742611021309',
        # 'https://news.baidu.com/widget?id=LadyNews&t=1742611021359'
    ]
    # <a href="http://baijiahao.baidu.com/s?id=1827247640418188253" mon="ct=0&amp;a=2&amp;c=internews&pn=1" target="_blank">“打着关税战还想要鸡蛋”</a></li>
    # <a href="http://baijiahao.baidu.com/s?id=1827260393988935916" mon="ct=0&amp;a=2&amp;c=internews&pn=2" target="_blank">以色列威胁“吞并”加沙部分地区 联合国警告“面粉仅..</a></li>
    # <a href="http://baijiahao.baidu.com/s?id=.*?" mon="ct=0&amp;a=2&amp;c=internews&pn=.*?" target="_blank">(.*?)</a></li>
    for url in url_list:
        html=get_html(url)
        news_list=parse_html(html)
        for news in news_list:
            print(news)
        # print(html.text)
        # print('=====================')