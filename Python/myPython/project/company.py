#!/usr/bin/python
# coding=utf-8

import requests

data_dict = {'code': 'mingyuan.ou', 'password': '/yuan15555136971'}

response = requests.post('http://bpowls.northking.net:7070/pm/userLogin!login.do', data=data_dict)

# http://bpowls.northking.net:7070/pm/userLogin!queryUserInfo.do

# response = requests.post('http://bpowls.northking.net:7070/pm/userLogin!queryUserInfo.do')

# data_dict = {'smUserByUserId.id': '8567'}

# response = requests.post('http://bpowls.northking.net:7070/pm/smUserRole!query.do', data=data_dict)   # 会返回登陆页面

print(response.url)

print(response.text)

# http://bpowls.northking.net:7070/pm/userLogin!queryUserInfo.do
