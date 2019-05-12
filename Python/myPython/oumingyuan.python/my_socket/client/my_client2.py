#!/usr/bin/python
# coding=utf-8

import socket

# 欧明跃的主机 IP
HOST = socket.gethostbyname(socket.gethostname())

# 欧明远的主机 IP
# HOST = '192.168.0.110'

PORT = 8888

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

# 向服务器发送请求
socket.send('dou bi')

receive_request = socket.recv(1024)

# 打印服务器响应信息到控制台
print 'below is the return message:'
print receive_request

socket.close()
