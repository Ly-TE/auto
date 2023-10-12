#!/user/bin/env python3
# -*- coding:utf-8 -*-

import requests
import json
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
url = 'https://api.bilibili.com/x/space/wbi/arc/search'
data = {
'mid': '170901672',
'ps': '30',
'tid': '0',
'pn': '1',
'keyword': '',
'order': 'pubdate',
'platform': 'web',
'web_location': '1550101',
'order_avoided': 'true',
'w_rid': 'e5b3ff6c4957dc2b1e9c76516ba87589',
'wts': '1686569270',
}
rqg = requests.get(url= url,headers=headers,params=data)
print(rqg.text)