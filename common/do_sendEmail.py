

# SMTP 是一种TCP协议支持的提供可靠且有效电子邮件传输的应用层协议

# 发送邮件的大致流程：
# ①设置邮件参数(邮箱服务器地址、发件人邮箱号、密码、收件人邮箱号……)
# ②设置邮件信息(主题、发件人名、内容、附件……)
# ③登录邮箱服务器
# ④登录邮箱账号
# ⑤发送邮件
# ⑥登出邮箱账号

import smtplib
from email.mime.text import MIMEText

#内容
class Do_sendEmail:
    def __init__(self):
        msg=''

    def send_email(self,msg,msg_from,mag_to,msg_subject):
        msg=MIMEText(msg,'plain','utf-8')
        msg['from']=msg_from
        msg['to']=mag_to
        msg['subject']=msg_subject


        #连接邮箱服务器
        s=smtplib.SMTP_SSL('smtp.exmail.qq.com','465')
        #用户名 客户端授权码
        s.login(msg_from, 'NAfPj4uXxAwTdr8u')

        #发送人 收件人 发送内容
        s.sendmail(msg_from,mag_to,str(msg))

        s.quit()

if __name__=='__main__':

    msg='hi,这是自动化测试邮件正文'
    Do_sendEmail().send_email(msg,'xumengrong@kiscloud.net','2444901244@qq.com','这是邮件主题')









'''

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人邮箱账号
my_sender='xumengrong@kiscloud.net'
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
my_pass = 'NAfPj4uXxAwTdr8u'
# 收件人邮箱账号
my_user='tianmei@kiscloud.net'

def mail():
    ret=True
    try:
        # 邮件内容
        msg=MIMEText('hi','plain','utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From']=formataddr(["wo",my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To']=formataddr(["ni",my_user])
        # 邮件的主题
        msg['Subject']="自动化测试--使用腾讯邮箱发送邮件测试"

        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender,[my_user,],msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception as e:
        raise  e
        ret=False
    return ret

ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print('失败')

'''















