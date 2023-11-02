# -*- coding: utf-8 -*-

import requests

url = "http://www.baidu.com"
params = {"id": "1001,1002"}
'''
传参方式
1.params = {"id": "1001"}
2.params = {"id": "1001,1002"}
3.params = {"id": "1001"，"kw":"北京"}
'''

rep = requests.get(url=url, params=params)
rep.encoding = 'utf-8'

print(rep.url)
print(rep.status_code)
print(rep.text)
