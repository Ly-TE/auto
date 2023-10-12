# -*- coding: utf-8 -*-
# author = 'API'
#function:测试用例的基类

import unittest
from common.project_path import *
from common.do_log import Log
from common.config import DoConfig
from common.do_request import DoRequest
from common.context import Context


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #登录需要数据
        config=DoConfig(conf_path)
        login_data=config.get_value('CASE_DATA','loginData')
        url=config.get_value('URL','url')
        login_url=url+config.get_value('CASE_DATA','login_url')
        login_methon=config.get_value('CASE_DATA','login_methon')
        #请求
        result=DoRequest(method=login_methon,url=login_url,data=login_data,headers=Context.headers).get_json()
        print(login_data)
        print(result)
        #加入token
        if result["data"]["token"]:
            setattr(Context, "token", result["data"]["token"])
            Context.headers["token"]=Context.token
            Log.debug('登录成功,获取到token：{}'.format(Context.token))

    # def test_a(self):
    #     print('aaa')

    @classmethod
    def tearDownClass(cls):
        if hasattr(Context,"token"):
            delattr(Context,"token")

if __name__=='__main__':
    unittest.main()

