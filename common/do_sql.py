# -*- coding: utf-8 -*-
# author = 'API'

import json
import pymysql
from common.do_log import Log
from common.project_path import *
from common.config import DoConfig
from common.context import Context

class DoMysql:
    def __init__(self,sql_num,database):
        #sql_num为1时，取SQL_CONFIG1里面的配置项
        if sql_num==1:
            SQL_CONFIG='SQL_CONFIG1'
            Log.debug('取online,SQL_CONFIG1标签里面的配置项')
        else:
            SQL_CONFIG='SQL_CONFIG2'
            Log.debug('取online,SQL_CONFIG2标签里面的配置项')
        #获取数据库连接信息
        host=DoConfig(conf_path).get_value(SQL_CONFIG,'host')
        user=DoConfig(conf_path).get_value(SQL_CONFIG,'user')
        password=DoConfig(conf_path).get_value(SQL_CONFIG,'password')
        # database=DoConfig(conf_path).get_value(SQL_CONFIG,'database')
        port=int(DoConfig(conf_path).get_value(SQL_CONFIG,'port')) #端口要转

        #连接数据库
        try:
            self.conn=pymysql.connect(host=host,user=user,password=password,database=database,
                                      port=port,charset="utf8",cursorclass=pymysql.cursors.DictCursor)
            self.cursor=self.conn.cursor() #获取游标
            Log.debug('连接数据库成功：host={}，user={}，password={}，database={}，port={}'.format(host,user,password,database,port))
        except Exception as e:
            Log.error('连接数据库失败：{}'.format(e))
            raise e

    #获取1条
    def get_one(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        return result

    #获取所有
    def get_all(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result

    #获取部分
    def get_many(self,sql,size=None):
        self.cursor.execute(sql)
        result=self.cursor.fetchmany(size)
        return result

    #关闭
    def sql_close(self):
        self.cursor.close()
        self.conn.close()
        Log.debug('断开数据库')

if __name__=='__main__':
    #一条
    # sql='select * from card where member_id="2000600418970900"'
    # res=DoMysql(1,database='ty-basic-member')
    # one=res.get_one(sql)
    # print(one)

    #所有
    # sql="SELECT * from  orders " \
    # "where pay_code='WEIXIN' " \
    # "and pay_method='0'" \
    # "and order_status='2' " \
    # "and shop_name='测试门店第二轮'" \
    # "and create_time like'2019-04-30%' and member_name ='戚欣欣'"
    # res=DoMysql(2,database='bi_test_crs_test')
    # all=res.get_all(sql)
    # for i in all:
    #     print(i)


    # sql='select max(phone_number)  from ty_sys_auth.sys_user'
    # my_sql=DoMysql(1,database='ty_sys_auth')
    # result=my_sql.get_one(sql)
    # print(type(int(result['max(phone_number)'])))


    # data={"roleIdList":["a613809e-43cc-11e9-a104-000c298281c3"],"status":"","username":"许","phoneNumber":""}
    # sql='select count(*) from sys_user t1,sys_user_role t2 where t1.id=t2.user_id  ' \
    #     'and t2.role_id ="{}" and t1.status={}' \
    #     'and t1.username like "%{}%"' \
    #     'and t1.phone_number like "%{}%"'.format(data["roleIdList"][0],data["status"],data["username"],data["phoneNumber"])

    # sql='select count(*) from sys_user t1,sys_user_role t2 where t1.id=t2.user_id and t2.role_id ="{}"  and t1.status="{}" and t1.username like "%%{}%%" ' \
    #     'and t1.phone_number like "%{}%" '.format(data["roleIdList"][0],data["status"],data["username"],data["phoneNumber"])
    # # print(data["roleIdList"][0],data["status"],data["username"],data["phoneNumber"])
    # my_sql=DoMysql(1,database='ty_sys_auth')
    # result=my_sql.get_one(sql)
    # print(result)

    # sql='select t1.*,t2.role_id from sys_user t1,sys_user_role t2 where t1.id=t2.user_id and phone_number={}'.format(data_1["phoneNumber"])
    # sql_result=my_sql.get_all(sql)
    # data_1="18911111193"
    # sql='select * from ty_sys_auth.sys_user where phone_number="{}"'.format(data_1)
    my_sql=DoMysql(1,database='ty_sys_auth')
    # sql_result=my_sql.get_one(sql)
    # print(sql_result)


    # # id_sql='select id from ty_sys_auth.sys_user where phone_number="{}"'.format(Context.phone)
    # id_sql='select id from ty_sys_auth.sys_org where  deleted="0" and sort_num="{}"'.format('8353')
    # print('id_sql为：',id_sql)
    # print(my_sql)
    # get_id=my_sql.get_all(id_sql)
    # print('get_id为',get_id)


    # id_sql='select * from ty_sys_auth.sys_role  where role_name="{}"'.format('新增角色190613_153310.1')
    # sql_result=my_sql.get_one(id_sql)
    # print(sql_result["merchant_id"])
    sql='''SELECT t1.*,t2.role_id FROM sys_user t1,sys_user_role t2
                                WHERE t1.id = t2.user_id AND deleted = '0'
                                AND t1.phone_number = "18911111487"'''
    sql_result=my_sql.get_all(sql)
    a=["5d200577-92e9-466d-82bf-1cb37ea9343b","33993fc8-72c1-4735-8cc6-286a556fbd0d"]

    print(sql_result[0]["username"])
    print(sql_result[0]["phone_number"])
    print(sql_result[0]["sex"])
    print(sql_result[0]["email"])
    print(sql_result[0]["org_id"])
    for i in sql_result:
        if i['role_id'] in a:
            print(i['role_id'])


    my_sql.sql_close()


'''
    # sql='select * from ty_sys_auth.sys_user where username ="许" and phone_number={}'.format("15100001117")
    my_sql=DoMysql(1,database='ty_sys_auth')
    # result=my_sql.get_one(sql)
    # print(result)

    sql2='select t1.*,t2.role_id from sys_user t1,sys_user_role t2 where t1.id=t2.user_id and phone_number={}'.format("15100001115")
    result2=my_sql.get_all(sql2)
    roleIdList=["d0be8e4d-733d-4316-a42f-a4cbaa472196","c2dea1c9-61ac-4812-a34f-2993f281ef78",
                "fa68d7c8-c7d9-4732-b69f-914989d6ff1f","5d200577-92e9-466d-82bf-1cb37ea9343b","1eafa742-2a5a-4aa7-bcf8-8176b2c28a77"]

    print(type(result2[0]["status"]))
    # for i in result2:
    #     # print(i['role_id'])
    #     # print(type(str(i['role_id'])) )#为type 'unicode'
    #     if str(i['role_id'])  in roleIdList:
    #         print(i)
'''









