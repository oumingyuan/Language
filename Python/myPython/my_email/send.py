#!/usr/bin/python
# coding=utf-8

import new_email
import my_db

# 你好，族员欧明跃，我是你们的大族长雅美，祝你生日快乐。

information = "你好，我是你们的小萌主，祝你圣诞节快乐。"

emailAddress = my_db.getmail()

print emailAddress

for address in emailAddress:

    new_email.send_email(address, information)

# new_email.send_email("1312810743@qq.com", information)
