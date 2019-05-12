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

# 请求数据获取
request_client = open('request.txt')
request_client_str = request_client.read()

# 向服务端发送请求数据
socket.send(request_client_str)

receive_request = socket.recv(1024)

# 打印服务器响应信息到控制台

if not receive_request:
    print 'ERROR'
else:
    print 'below is the return message:'
    print receive_request


socket.close()
