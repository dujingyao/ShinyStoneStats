# https://xinxiang.ke.com/ershoufang/
# https://xinxiang.ke.com/ershoufang/pg2/
# https://xinxiang.ke.com/ershoufang/pg3/
import requests
import re
import csv
def get_html(url,time=10):
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
    pattern = r'<img class="lj-lazy".*?alt="(.*?)" title="(.*?)">'
    rooms = re.finditer(pattern, res.text, re.S)
    room_list = []
    for room in rooms:
        alt=room.group(1)
        title = room.group(2)
        room_list.append([alt, title])
    return room_list

def save_data(data):
    with open('rooms.csv', 'a', newline="", encoding="utf-8") as f:
        # writer = csv.writer(f)
        for item in data:
            f.write(item)
        f.write('\n')

if __name__ == '__main__':
    url='https://xinxiang.ke.com/ershoufang/'
    html=get_html(url)
    # print(html.text)
    room_list = parse_html(html)
    print('第1页：')
    for room in room_list:
        print(room)
        save_data(room)
    for i in range(2,6):
        print(r'第{}页：'.format(i))
        url_page=url+'pg'+str(i)+'/'
        html = get_html(url)
        # print(html.text)
        room_list = parse_html(html)
        for room in room_list:
            print(room)
            save_data(room)
