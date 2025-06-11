import requests
import csv
import json

def get_html(url, headers):
    """获取网页内容"""
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    response.raise_for_status()
    return response.text

def parse(json_text):
    """解析JSON数据，提取医生姓名和擅长领域"""
    try:
        data = json.loads(json_text)
        doctor_list = []

        # 检查JSON结构
        if 'doctors' in data:
            doctor_items = data['doctors']
        elif 'data' in data and 'list' in data['data']:
            doctor_items = data['data']['list']
        else:
            print("未找到预期的数据结构")
            return doctor_list

        for item in doctor_items:
            # 获取医生姓名
            staff_name = item.get('STAFF_NAME', '未知')

            # 获取擅长领域
            skill_field = item.get('DEP_NAME', '未知')
            # 如果擅长领域不存在，尝试获取其他可能包含类似信息的字段
            if skill_field == '未知':
                skill_field = item.get('SKILL', item.get('SKILL_DESC', item.get('STAFF_DESC', '未知')))

            doctor_list.append({
                'name': staff_name.strip() if isinstance(staff_name, str) else str(staff_name),
                'skill': skill_field.strip() if isinstance(skill_field, str) else str(skill_field)
            })

        return doctor_list
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return []
    except Exception as e:
        print(f"解析过程中出错: {e}")
        return []

if __name__ == "__main__":
    # API基础URL
    start_url = "http://www.bspider.top/jkwin/getDoctorList?areaId=42&depId=&hasDuty=&pageSize=10&pageNo="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # 准备CSV文件
    csv_file = 'doctor_skills.csv'
    fieldnames = ['name', 'skill']

    # 创建CSV文件并写入表头
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    # 爬取多页数据
    all_doctors = []
    for i in range(1, 11):
        try:
            url = start_url + str(i)
            print(f"正在爬取第{i}页...")
            json_text = get_html(url, headers)

            doctor_list = parse(json_text)
            all_doctors.extend(doctor_list)

            # 将数据写入CSV文件
            with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for doctor in doctor_list:
                    writer.writerow(doctor)

            print(f"第{i}页数据爬取成功，获取{len(doctor_list)}条记录")
        except Exception as e:
            print(f"爬取第{i}页时出错: {e}")

    print(f"爬取完成，共获取{len(all_doctors)}条医生数据，已保存到{csv_file}")