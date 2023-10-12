import requests

rep = requests.request()

# 返回字符串数据
print(rep.text)
# 返回字节数据
print(rep.content)
# 返回字典数据
print(rep.json())
# 状态码
print(rep.status_code)
# 返回状态信息
print(rep.reason)
# 返回cookie信息
print(rep.cookies)
# 返回编码格式
print(rep.encoding)
# 返回响应头信息
print(rep.headers)
