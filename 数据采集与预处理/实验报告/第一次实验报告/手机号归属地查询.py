import requests
import re

def get_phone_location(phone):
    url = f"https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as error:
        print(f"请求错误：{error}")
        return None

def parse_location(html):
    pattern = r'<td><span>([^<]+)\s*<a[^>]+>([^<]+)</a></span></td>'
    match = re.search(pattern, html)
    if match:
        province = match.group(1).strip()
        city = match.group(2).strip()
        return f"{province}{city}"
    return None

if __name__ == '__main__':
    phone = "18864611446"
    html = get_phone_location(phone)
    if html:
        location = parse_location(html)
        if location:
            print(f"手机号 {phone} 的归属地是：{location}")