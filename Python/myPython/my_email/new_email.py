#!/usr/bin/python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(receivers, information):
    mail_host = "smtp.qq.com"  # 设置第三方 SMTP 服务
    sender = 'oumingyuan@foxmail.com'  # 发件箱
    mail_user = "雅美"  # 发件人姓名
    mail_pass = "lztokxmiblfzbice"  # 口令

    message = MIMEText(information, 'plain', 'utf-8')
    message['From'] = Header(mail_user, 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = '江左盟萌主邮件通知'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')

    try:

        smtpObj = smtplib.SMTP_SSL(mail_host, 465)

        smtpObj.login(sender, mail_pass)

        smtpObj.sendmail(sender, receivers, message.as_string())

        print "邮件发送成功"

    except smtplib.SMTPException:

        print "Error: 无法发送邮件"
