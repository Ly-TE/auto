import requests


class TestApi:
    # 类变量
    access_token = ""

    # 获取access_token鉴权码接口
    def test_get_token(self):
        urls = "https://api.weixin.qq.com/cgi-bin/token"  # 获取access_token的API地址
        datas = {
            "grant_type": "client_credential",  # 授权类型为客户端凭证
            "appid": "wx51f605c204d32479",  # 应用ID
            "secret": "4d90172f3c8d290c44409d1999893ccf"  # 应用密钥
        }
        try:
            res = requests.post(url=urls, params=datas)  # 发送POST请求
            print(res.json())  # 打印返回的json数据
            res.raise_for_status()  # 如果返回状态码不是200，抛出异常
            TestApi.access_token = res.json()["access_token"]  # 从返回的json数据中获取access_token，保存到类变量中
            print(TestApi.access_token)
        except requests.exceptions.RequestException as e:
            print("发生异常:", e)

    # 查询标签接口
    def test_select_flag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/get"  # 查询标签的API地址
        datas = {
            "access_token": TestApi.access_token  # 通过类变量获取access_token
        }
        try:
            res = requests.get(url=urls, params=datas)  # 发送GET请求
            res.raise_for_status()  # 如果返回状态码不是200，抛出异常
            print(res.json())  # 打印返回的json数据
        except requests.exceptions.RequestException as e:
            print("发生异常:", e)

    # 编辑标签接口
    def test_edit_flag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestApi.access_token  # 编辑标签的API地址，通过类变量获取access_token
        payload = {
            'id': 120,  # 标签ID
            'name': '广东人111'  # 修改后的标签名称
        }
        try:
            res = requests.post(url=urls, json=payload)  # 发送POST请求，并将修改标签的数据作为Json数据发送到API
            res.raise_for_status()  # 如果返回状态码不是200，抛出异常
            print(res.json())  # 打印返回的json数据
        except requests.exceptions.RequestException as e:
            print("发生异常:", e)

    # 文件上传接口
    def test_files_upload(self):
        urls = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"  # 文件上传的API地址
        datas = {
            "access_token": TestApi.access_token  # 通过类变量获取access_token
        }
        files = {
            "media": open("E:/shu.jpg", "rb")  # 要上传的文件路径，这里假设为 E:/shu.jpg
        }
        try:
            res = requests.post(url=urls, files=files, params=datas)  # 发送POST请求，并将文件作为二进制流发送到API
            res.raise_for_status()  # 如果返回状态码不是200，抛出异常
            print(res.json())  # 打印返回的json数据
        except requests.exceptions.RequestException as e:
            print("发生异常:", e)


if __name__ == '__main__':
    test_api = TestApi()  # 创建TestApi类的实例
    test_api.test_get_token()  # 调用获取access_token的方法
    test_api.test_select_flag()  # 调用查询标签的方法
    test_api.test_edit_flag()  # 调用编辑标签的方法
    test_api.test_files_upload()  # 调用文件上传的方法
