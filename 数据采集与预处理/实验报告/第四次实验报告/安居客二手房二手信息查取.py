import requests
from lxml import etree
import csv, pymysql

def get_html(url, headers):
    """
    获取网页源码
    :param url: 网页地址
    :param headers: 请求头
    :return: 网页源码
    """
    try:
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None

def parse(html):
    doc = etree.HTML(html)
    out_list = []

    for row in doc.xpath('//div[@class="property"]'):
        title = row.xpath('a//h3/text()')[0].strip()
        info = row.xpath('string(./a//*[@class="property-content-info"])')
        info = info.replace(" ", "").replace("\n\n", "\n").split("\n")

        # 楼盘名称
        house = row.xpath("a//*[@class='property-content-info-comm-name']/text()")[0]
        # 地址
        address = row.xpath("string(./a//*[@class='property-content-info-comm-address'])")
        # 价格
        price = row.xpath("a//*[@class='property-price-average']/text()")[0]
        price = price.replace(" ", "")

        row_list = [
            title.strip(),  # 卖点标题
            house.strip(),  # 楼盘
            address.strip(),  # 地址
            info[0] if len(info) >= 1 else "",  # 房屋户型
            info[1] if len(info) >= 2 else "",  # 建筑面积
            info[3] if len(info) >= 4 else "",  # 所在楼层
            info[4] if len(info) >= 5 else "",  # 建造年代
            price  # 房价
        ]
        out_list.append(row_list)

    return out_list

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['标题', '楼盘', '地址', '户型', '面积', '楼层', '年代', '价格'])
        writer.writerows(data)

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    base_url = 'http://www.bspider.top/anjuke/?page='
    all_data = []  # 用于保存所有页面的数据

    # 爬取第1页到第9页
    for page in range(1, 10):  # 1到9页
        url = base_url + str(page)
        print(f"正在爬取第{page}页: {url}")

        html = get_html(url, headers)
        if not html:
            print(f"获取第{page}页失败，跳过")
            continue

        data = parse(html)  # 修改parse函数只返回数据列表
        all_data.extend(data)

        # 添加随机延时防止被封
        import time, random
        time.sleep(random.uniform(1, 3))

    # 保存数据
    if all_data:
        save_to_csv(all_data, 'anjuke.csv')
        print(f"共爬取{len(all_data)}条房源信息")
    else:
        print("未获取到任何数据")