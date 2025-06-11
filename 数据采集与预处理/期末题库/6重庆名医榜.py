#爬取1-3页的名医榜数据信息（STAFF_NAME和STAFF_TYPE），
# 网址http://www.bspider.top/jkwin，
# 结果存放到“名医榜.csv”，保存在datas目录中，如果目录不存在，先创建目录。
import requests
import csv
import json
import os
# 确保datas目录存在
# 如果不存在则会自动创建
os.makedirs('datas', exist_ok=True)
def get_html(url,headers):
    response=requests.get(url=url,headers=headers)
    response.encoding=response.apparent_encoding
    response.raise_for_status()
    return response.text

def parse(json_text):
    data = json.loads(json_text)
    doctor_list = []
    for item in data['doctors']:
        staff_name = item.get('STAFF_NAME')
        staff_type = item.get('STAFF_TYPE')
        if staff_name and staff_type:
            doctor_list.append({
                'name': staff_name.strip(),
                'type': staff_type.strip()
            })
    return doctor_list

if __name__=="__main__":
    start_url = "http://www.bspider.top/jkwin/getDoctorList?areaId=42&depId=&hasDuty=&pageSize=10&pageNo="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 准备CSV文件
    csv_file = '名医榜.csv'
    fieldnames = ['name', 'type']

    # 创建CSV文件并写入表头
    with open('./datas/'+csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    for i in range(1,4):
        url=start_url+str(i)
        json_text=get_html(url,headers)
        # print(json_text)
        doctor_list=parse(json_text)
        print(doctor_list)
        # 保存至csv文件中
        # 将数据写入CSV文件
        with open('./datas/'+csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for doctor in doctor_list:
                writer.writerow(doctor)