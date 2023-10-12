# -*- coding: utf-8 -*-
# author = 'API'

import json
import unittest
from ddt import ddt,data
from common.do_log import Log
from common.config import DoConfig
from common.context import Context,Regex
from common.project_path import *
from common.do_excel import DoExcel
from common.do_request import DoRequest
from common.do_sql import DoMysql
from testcase.base_test import TestBase

#获取测试数据
cases=DoExcel(data_path,'updateUser').get_value()

@ddt
class TestUpdateUser(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Log.info('开始{}模块的测试'.format('编辑员工'))
        Log.debug("连接数据库")
        global my_sql
        my_sql=DoMysql(1,database='ty_sys_auth')

    def setUp(self):
        phone_sql='select max(phone_number) from ty_sys_auth.sys_user'
        try:
            self.phone_result=DoMysql(1,database='ty_sys_auth').get_one(phone_sql)
            self.phoneNumber=str(int(self.phone_result['max(phone_number)'])+1)
            if hasattr(Context,'phone'):
                Context.phone=self.phoneNumber
            else:
                setattr(Context,'phone',self.phoneNumber)
        except Exception as e:
            Log.error(e)
            raise e

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        delattr(Context,'phone')
        delattr(Context,'id')
        my_sql.sql_close()
        Log.debug("关闭数据库连接")
        Log.info('结束{}模块的测试'.format('编辑员工'))

    @data(*cases)
    def test_updateUser(self,case):
        new_data=Regex.regex(case.data)
        Log.info('测试第{}条用例，标题是:"{}"，测试数据是：\n{}'.format(case.id,case.title,new_data))
        #进行请求
        result=DoRequest(case.method,case.url,new_data.encode(),headers=Context.headers).get_json()
        Log.info('测试结果{}'.format(result))

        #新增成功 查询结果断言
        try:
            self.assertEqual(eval(case.expected)["message"],result['message'])
            Log.info('测试结果pass')

            #查数据库
            data_1=json.loads(new_data)
            if result['message']=='保存成功！':
                sql_add='''SELECT t1.*,t2.role_id
                          FROM  sys_user t1, sys_user_role t2
                         WHERE  t1.id = t2.user_id AND deleted = '0'
                           AND  t1.phone_number="{}" '''.format(data_1["phoneNumber"])
                sql_add_result=DoMysql(1,database='ty_sys_auth').get_all(sql_add)

                #新增成功  获取用户id
                if case.id==1:
                    setattr(Context,'id',sql_add_result[0]['id'])
                    Log.info('新增员工手机号：{},获取到的id:{}'.format(self.phoneNumber,sql_add_result[0]['id']))

                #编辑成功  检查数据库
                else:
                    self.assertEqual(data_1["username"],sql_add_result[0]["username"])
                    self.assertEqual(int(data_1["sex"]),sql_add_result[0]["sex"])
                    self.assertEqual(data_1["email"],sql_add_result[0]["email"])
                    self.assertEqual(data_1["phoneNumber"],sql_add_result[0]["phone_number"])
                    self.assertEqual(data_1["merchantId"],sql_add_result[0]["merchant_id"])
                    self.assertEqual(data_1["orgId"],sql_add_result[0]["org_id"])
                    for i in sql_add_result:#角色
                        self.assertIn(str(i['role_id']),data_1["roleIdList"])
                    Log.info('数据库校验pass')
        except AssertionError as e:
            Log.error('测试结果fail:{}'.format(e))
            raise e

if __name__=='__main__':
    unittest.main()