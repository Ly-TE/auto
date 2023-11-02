# -*- coding: utf-8 -*-

import unittest
import requests


# 新建测试类--unittest.TestCase
class TestLogin(unittest.TestCase):
    # setup test方法开始执行之前，首先会被执行
    def setUp(self):
        # 获取session对象
        self.session = requests.session()
        # 登录url
        self.url_login = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
        # 验证码url
        self.url_verrify_code = "http://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify"

    # teardown test方法开始执行之后，首先会被执行

    def tearDown(self):
        # 关闭session对象
        self.session.close()

    # case1登录成功

    def test_login_success(self):
        # 请求验证码 --获取cookies
        self.session.get(self.url_verrify_code)
        # 请求登录
        data = {
            "username": "13997505254",
            "password": "13997505254",
            "verify_code": 8888
        }
        r = self.session.post(self.url_login, data=data)
        try:
            # 断言
            self.assertEqual("登陆成功", r.json()["msg"])
        except AssertionError as e:
            print(e)

    # case2登录失败  账号不存在
    def test_username_not_exit(self):
        # 请求验证码 --获取cookies
        self.session.get(self.url_verrify_code)
        # 请求登录
        data = {
            "username": "139975052541",
            "password": "13997505254",
            "verify_code": 8888
        }
        r = self.session.post(self.url_login, data=data)
        try:
            # 断言
            self.assertEqual("账号不存在!", r.json()["msg"])
        except AssertionError as e:
            print(e)

    # case3登录失败  密码错误
    def test_password_error(self):
        # 请求验证码 --获取cookies
        self.session.get(self.url_verrify_code)
        # 请求登录
        data = {
            "username": "13997505254",
            "password": "139975052541",
            "verify_code": 8888
        }
        r = self.session.post(self.url_login, data=data)
        try:
            # 断言
            self.assertEqual("密码错误!", r.json()["msg"])
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
