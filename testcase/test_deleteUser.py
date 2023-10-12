# -*- coding: utf-8 -*-
# author = 'API'

import json
import unittest
from ddt import ddt,data
from common.do_log import Log
from common.context import Context,Regex
from common.project_path import *
from common.do_excel import DoExcel
from common.do_request import DoRequest
from common.do_sql import DoMysql
from testcase.base_test import TestBase

#获取测试数据
cases=DoExcel(data_path,'deleteUser').get_value()

@ddt
class TestDeleteUser(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Log.info('开始{}模块的测试'.format('删除员工'))
        Log.debug("连接数据库")
        cls.my_sql=DoMysql(1,database='ty_sys_auth')
        phone_sql='select max(phone_number) from ty_sys_auth.sys_user'
        try:
            phone_result=cls.my_sql.get_one(phone_sql)
            cls.phoneNumber=str(int(phone_result['max(phone_number)'])+1)
            setattr(Context,'phone',cls.phoneNumber)
        except Exception as e:
            Log.error(e)
            raise e

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        delattr(Context,'phone')
        delattr(Context,'id')
        cls.my_sql.sql_close()
        Log.debug("关闭数据库连接")
        Log.info('结束{}模块的测试'.format('删除员工'))

    @data(*cases)
    def test_deleteUser(self,case):
        new_data=Regex.regex(case.data)
        Log.info('测试第{}条用例，标题是:"{}"，测试数据是:\n{}'.format(case.id,case.title,new_data))
        #进行请求
        result=DoRequest(case.method,case.url,new_data.encode(),headers=Context.headers).get_json()
        Log.info('测试结果{}'.format(result))

        #结果断言
        try:
            self.assertEqual(eval(case.expected)["message"],result['message'])
            Log.info('测试结果pass')

            #查数据库
            sql='select * from ty_sys_auth.sys_user where phone_number="{}"'.format(self.phoneNumber)
            sql_result=DoMysql(1,database='ty_sys_auth').get_one(sql)

            #新增成功  获取用户id
            if result['message']=='保存成功！' :
                if hasattr(Context,'id'):
                    Context.id=sql_result['id']
                else:
                    setattr(Context,'id',sql_result['id'])
                Log.info('获取到的id:{}'.format(self.phoneNumber,sql_result['id']))

            #删除成功  检查数据库
            elif result['message']=='删除成功！' :
                self.assertEqual(1,sql_result['deleted']) #删除后为1
                Log.info('删除的手机号码为：{}'.format(Context.phone))
        except AssertionError as e:
            Log.error('测试结果fail:{}'.format(e))
            raise e

if __name__=='__main__':
    unittest.main()