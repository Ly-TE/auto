# -*- coding: utf-8 -*-

import requests

session = requests.session()

url_verrify_code = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify"

session.get(url_verrify_code)

url_login = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
data = {
    "username": "13997505254",
    "password": "13997505254",
    "verify_code": 8888
}

r = session.post(url=url_login, data=data)
print(r.json())

url_order = "http://hmshop-test.itheima.net/Home/Order/order_list.html"
r = session.get(url=url_order)
print(r.text)
