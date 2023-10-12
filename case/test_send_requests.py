# import requests
#
# rep = requests.request()
# # 返回字符串的数据
# print(rep.text)
# # 返回字节格式的数据
# print(rep.content)
# # 返回字典格式的数据
# print(rep.json())
# # 状态码
# print(rep.status_code)
# # 返回状态信息
# print(rep.reason)
# # 返回cookie信息
# print(rep.cookies)
# # 返回编码格式
# print(rep.encoding)
# # 返回响应头信息
# print(rep.headers)
import json
import re
import pytest
import requests


class TestSendRequest:
    access_token = ''
    csrf_token = ''

    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx51f605c204d32479",
            "secret": "4d90172f3c8d290c44409d1999893ccf"
        }
        rep = requests.get(url=url, params=data)
        print(rep.json())
        TestSendRequest.access_token = rep.json()['access_token']
        raise Exception('1111')

    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestSendRequest.access_token + ""
        data = {"tag": {"id": 134, "name": "广东人"}}
        # rep = requests.post(url=url, json=data)
        # json.dumps(data)序列化  把字典格式的数据转换成str格式
        # json.loads(data)反序列化 把str格式转换成字典格式
        rep = requests.post(url=url, data=json.dumps(data))
        print(rep.json())

    def test_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + TestSendRequest.access_token + ""
        data = {
            "media": open(r"E:\shu.png", "rb")
        }
        rep = requests.post(url=url, files=data)
        print(rep.json())

    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        rep = requests.get(url=url)
        print(rep.text)
        # 通过正则表达式获取鉴权码
        TestSendRequest.csrf_token = re.search('name="csrf_token" value="(.*?)"', rep.text)[1]

    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            'username': 'msxy',
            'password': 'msxy',
            'csrf_token': TestSendRequest.csrf_token,
            'backurl': 'http://47.107.116.139/phpwind/',
            'invite': ''
        }
        headers = {
            'Accept': 'application/json,text/javascript,/;q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }
        rep = requests.post(url=url, data=data, headers=headers)
        print(rep.text)


'''
运行方式
1.主函数的方式（命令行的方式）
-v 输出更加详细的运行信息
-s 输出调试信息
-n 多线程运行
--reruns 数字    失败用例重跑
--html=报告的路径
'''
if __name__ == '__main__':
    pytest.main(['-vs', '--reruns=2', '--html=C:/Users/admin/Desktop/work/report.html'])
