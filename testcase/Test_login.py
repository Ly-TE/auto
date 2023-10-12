# -*- coding: utf-8 -*-
# author = 'API'
# function:登录测试用例

import json
import unittest

from ddt import ddt, data

from common.context import Context, Regex
from common.do_excel import DoExcel
from common.do_log import Log
from common.do_request import DoRequest
from common.project_path import *

# 获取测试数据
cases = DoExcel(data_path, 'login').get_value()


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Log.info('开始{}模块的测试'.format('登录'))

    @classmethod
    def tearDownClass(cls):
        Log.info('结束{}模块的测试'.format('登录'))

    @data(*cases)
    def test_login(self, case):
        # 进行请求
        new_data = Regex.regex(case.data)
        Log.info('执行第{}条用例，标题是:"{}"，测试数据是\n{}'.format(case.id, case.title, new_data))
        result = DoRequest(case.method, case.url, new_data, headers=Context.headers).get_json()  # data是str，这个项目不用转为字典
        # 断言
        try:
            if case.title == '正常登录':  # 返回的消息errorcode和message都是空的，无法来做断言
                Log.info('测试结果,成功登陆，获取到token：{}'.format(result["data"]['token']))
                self.assertIsNotNone(result["data"]['token'])
            else:
                Log.info('测试结果{}'.format(result))
                self.assertEqual(json.loads(case.expected)["message"], result["message"])
            Log.info('测试结果断言成功')
        except AssertionError as e:
            Log.error('断言失败：{}'.format(e))
            raise e


if __name__ == '__main__':
    unittest.main()
