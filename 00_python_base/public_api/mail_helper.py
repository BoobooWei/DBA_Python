# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.18.07.09.0
Description: 邮件发送接口
Help:
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailHelper:
    def __init__(self, **kwargs):
        self.from_user = kwargs['from_user']
        self.from_pass = kwargs['from_pass']
        self.to_users = kwargs['to_users']
        self.post_host = kwargs['post_host']
        self.post_port = kwargs['post_port']
        self.tbody = kwargs['tbody']
        self.msg = MIMEMultipart('related')

    def get_subject(self, ):
        """
        邮件标题
        :return:
        """
        subject = "{}".format("每日告警通知")
        return subject

    def get_body(self):
        """
        邮件正文
        :return:
        """
        content = "<p>{0}</p>".format(self.tbody)
        msgtext = MIMEText(content, "html", "UTF-8")
        return msgtext

    def send_mail(self):
        msgtext = self.get_body()
        self.msg.attach(msgtext)
        self.msg['Subject'] = self.get_subject()
        self.msg['From'] = self.from_user
        if len(self.to_users) > 1:
            self.msg['To'] = ",".join(self.to_users)
        else:
            self.msg['To'] = self.to_users
        try:
            server = smtplib.SMTP_SSL()
            server.connect(self.post_host, self.post_port)
            server.set_debuglevel(1)
            server.login(self.from_user, self.from_pass)
            server.sendmail(self.from_user, self.to_users, self.msg.as_string())
            server.quit()
            print "发送成功"
        except Exception as e:
            print str(e)


if __name__ == "__main__":
    """
    QQ邮箱配置帮助，需要开启第三方程序访问功能
    https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
    """
    mail_params = {
        'from_user': 'xxx@qq.com',
        'from_pass': 'xx',
        'post_host': 'smtp.qq.com',  # Smtp服务
        'post_port': '465',  # SMTP 端口
        'to_users': ['xx@hotmail.com', 'xx@qq.com'],
        'tbody': "一切正常",
    }
    api = MailHelper(**mail_params)
    api.send_mail()

