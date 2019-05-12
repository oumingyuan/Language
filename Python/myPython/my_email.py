#!/usr/bin/python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText


# the method used to send email to someone
def send_email(address_of_receive):
    # the information of the service
    address_of_send = "oumingyuan@foxmail.com"
    password_of_send = "tfbrbbfsewndbjhe"

    # the detail of the email
    msg = MIMEText("你好，欧氏家族成员。收到请别回信，我是你们的大萌主雅美，祝你生活愉快。")  # 邮件内容
    msg["Subject"] = "江左盟萌主邮件通知"  # 邮件主题
    msg["From"] = address_of_send
    msg["To"] = address_of_receive

    s = smtplib.SMTP_SSL("smtp.qq.com", 465)

    s.login(address_of_send, password_of_send)
    s.sendmail("yamei", address_of_receive, msg.as_string())
    s.quit()

    print("send email success")


send_email("709336535@qq.com")
