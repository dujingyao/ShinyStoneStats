import requests
from urllib import parse
def get_html(url,time=10):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    try:
        r=requests.get(url,headers=headers,timeout=time)
        r.encoding=r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as error:
        print(error)
if __name__=='__main__':
    parm={
        'mobile':'18864611446',
        'action':'mobile'
    }
    p=parse.urlencode(parm)
    url='https://www.ip138.com/mobile.asp?'
    url=url+p
    x=get_html(url)
    print(x)