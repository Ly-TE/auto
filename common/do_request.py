# -*- coding: utf-8 -*-
# author = 'API'


import json
import requests
from common.do_log import Log

class DoRequest:
    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method=='get':
                self.result=requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method=='post':#传入的data要是字符串   加请求头
                self.result=requests.post(url=url,data=data,cookies=cookies,headers=headers)
        except Exception as e:
            Log.error('执行请求失败：{}'.format(e))
            raise e

    def get_statuscode(self):
        return self.result.status_code

    def get_json(self):
        return self.result.json()

    def get_text(self):
        return self.result.text

if __name__=='__main__':
    url='http://10.100.50.12:8215/oms/merchant/login'
    data='{"loginName":"15100001111","password":"55722118e8b7648e5385b65528a77712"}'
    headers={"content-type":"application/json"}
    # result=requests.request('post',url,data=data,headers=headers).json()
    # print(result)

    t=DoRequest('post',url,data,headers=headers)
    # print(t.get_text())
    # print(json.dumps(t.get_json(),indent=4))


    query_data={"pageIndex":0,"pageSize":10,"merchantId":"40ed3fb4-6b8a-4606-9cb3-a1e8bba5584b","orgId":None,"roleIdList":[],"status":"","username":""}
    query_data["phoneNumber"]="18911111149"

    query_url='http://10.100.50.12:8215/oms/merchant/user/query'
    headers_1={'token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTEwMDAwMTExMSIsImV4cCI6MTU1OTI1MDc1MCwiaWF0IjoxNTU5MjA3NTUwfQ.jOac_c5DekDADuwt2JzKcY7_cn25uqAs43NsFpFCb-2rFt_25SJ_K26ORz-Ro1mvkhTsHA_3_9I6MnRA1E-IrQ', 'content-type': 'application/json'}

    query_result=DoRequest('post',query_url,json.dumps(query_data).encode(),headers=headers_1).get_json()
    print(query_result['data']['total'])

    # print(query_data["pageIndex"])


















