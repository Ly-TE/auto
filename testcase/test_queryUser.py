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
cases=DoExcel(data_path,'queryUser').get_value()

@ddt
class TestUserQuery(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Log.info('开始{}模块的测试'.format('查询员工'))
        Log.debug("连接数据库")
        global my_sql
        my_sql=DoMysql(1,database='ty_sys_auth')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        my_sql.sql_close()
        Log.debug("关闭数据库连接")
        Log.info('结束{}模块的测试'.format('查询员工'))

    @data(*cases)
    def test_userQuery(self,case):
        #进行请求
        new_data=Regex.regex(case.data)
        Log.info('测试第{}条用例，标题是:"{}"，测试数据是\n{}'.format(case.id,case.title,new_data))
        result=DoRequest(case.method,case.url,new_data.encode(),headers=Context.headers).get_json()
        Log.info('查询出的数据条数：{}'.format(result['data']['total']))

        #查询数据库
        data_1=json.loads(new_data)
        sql='''SELECT t1.*,t2.role_id
               FROM sys_user t1,sys_user_role t2
              WHERE t1.id = t2.user_id
                AND t2.role_id  LIKE "%{}%"
                AND t1.STATUS LIKE "%{}%"
                AND t1.username LIKE "%{}%"
                AND t1.phone_number LIKE "%{}%"
                AND t1.org_id LIKE "%{}%" '''.format(data_1["roleIdList"][0],data_1["status"],
                                                     data_1["username"],data_1["phoneNumber"],data_1["orgId"])
        sql_result=my_sql.get_all(sql)
        try:
            #新增成功 查询结果断言
            self.assertEqual(len(sql_result),result['data']['total'])
            Log.info('测试结果pass')

            #比对具体信息
            if result['data']['total']==1:
                self.assertEqual(data_1["username"],sql_result[0]["username"])
                self.assertEqual(data_1["phoneNumber"],sql_result[0]["phone_number"])
                self.assertEqual(data_1["merchantId"],sql_result[0]["merchant_id"])
                self.assertEqual(data_1["orgId"],sql_result[0]["org_id"])
                self.assertEqual(int(data_1["status"]),sql_result[0]["status"])
                for i in sql_result:#角色
                    self.assertIn(str(i['role_id']),data_1["roleIdList"])
                Log.info('数据库校验pass')
        except AssertionError as e:
            Log.error('测试结果fail:{}'.format(e))
            raise e

if __name__=='__main__':
    unittest.main()