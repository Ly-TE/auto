# -*- coding: utf-8 -*-
# author = 'API'

import re
from common.project_path import *
from common.config import DoConfig
from common.do_excel import DoExcel

class Context:
    config=DoConfig(conf_path)
    headers={"content-type":"application/json"}
    login_data = None

    #商户id
    merchantId=config.get_value('CASE_DATA','merchantId')
    # 组织id
    orgId=config.get_value('CASE_DATA','orgId')
    orgId_2=config.get_value('CASE_DATA','orgId_2')
    #操作系统id
    appId=config.get_value('CASE_DATA','appId')
    #赋权
    resIdList=config.get_value('CASE_DATA','resIdList')
    #角色名称
    pre_roleName=config.get_value('CASE_DATA','pre_roleName')
    pre_roleid=config.get_value('CASE_DATA','pre_roleid')
    #角色列表
    pre_roleidList=config.get_value('CASE_DATA','pre_roleidList')

    #登录模块测试数据
    login_phone=config.get_value('CASE_DATA','login_phone')
    password=config.get_value('CASE_DATA','password')
    username=config.get_value('CASE_DATA','username')


#上下文管理器
class Regex:
    @staticmethod
    def regex(string):
        pattern='#{(.*?)}'
        while re.search(pattern, string):
            key=re.search(pattern, string).group(1)
            value=getattr(Context,key)
            string=re.sub(pattern,value,string,count=1)
        return string

if __name__=='__main__':
    # print(Context.headers)
    print(Context.pre_roleName)
    # cases=DoExcel(data_path,'updateUser').get_value()
    # for i in cases:
    #     res=Regex.regex(i.data)
    #     print(res)


