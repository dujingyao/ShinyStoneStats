import urllib.request

url = 'https://weibo.com/u/6345813354'

headers = {
    'cookie':'XSRF-TOKEN=2en0R4gtgwfCLsLJ8XDng94Z; SCF=Apm4CECPIABmLTYXg7Nyxhk8w3hs-LDnaSY9AB0qor_rz-TJPbqewSOxxSXfptCz8kF4edTfgeJy22HK3I88oq4.; SUB=_2A25KZgHJDeRhGeBN71cZ8S3PzjiIHXVpGhsBrDV8PUNbmtANLWfZkW9NRHNY3jSfcYBRhtbNHE-sa0rG07tOuUk5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF9dXkRdmRebL_3vyA_aZkT5NHD95Qce0Bf1h20e0-XWs4DqcjNi--fiK.ciKLhi--ci-8hi-2Ei--fiKysi-8si--NiKnRi-zpi--fi-z7iKysi--NiKyhi-8FP7tt; ALF=02_1737096857; _s_tentry=weibo.com; Apache=7215517039105.696.1734505173276; SINAGLOBAL=7215517039105.696.1734505173276; ULV=1734505173342:1:1:1:7215517039105.696.1734505173276:; WBPSESS=TG1x595n2DOGSIGs1-sLdcT2q4e0KaUzqWfFUAva05FF4-h9ikNbXheeMdXQRQGnCnllaIsYublb_d_HEq_3EHSKxMt5hYqigvA8sPZwK3WHhRMSBNIueQMdTKT17bL3zt0BLJkcA9dCIvx0_zBdTw=='
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)