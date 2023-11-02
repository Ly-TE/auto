# -*- coding: utf-8 -*-

import requests

# 请求验证码
url_verrify_code = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify"
# 获取cookies
r = requests.get(url_verrify_code)
r_cookies = r.cookies
print("获取的cookies为", r_cookies["PHPSESSID"])

# 设置cookies变量
cookies = {"PHPSESSID": r_cookies["PHPSESSID"]}

# 调用post方法，
url_login = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
data = {
    "username": "13997505254",
    "password": "13997505254",
    "verify_code": 8888
}

r = requests.post(url=url_login, data=data, cookies=cookies)
print(r.json())

# 查询订单
url_order = "http://hmshop-test.itheima.net/Home/Order/order_list.html"
r = requests.get(url=url_order, cookies=cookies)
print(r.text)
