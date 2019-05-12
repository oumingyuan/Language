#!/usr/bin/python
# coding=utf-8

import socket
import time

# socket 的初始化
# HOST = '192.168.0.110'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8888

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))

# 监听,最多允许10个连接
socket.listen(10)

local_request = open('request.txt')
local_request_message = local_request.read()
response = open('response.txt')

# 服务器判断逻辑
# 设置死循环等待客户端连接,直至等待时间结束或进程结束
while True:

    connection, address = socket.accept()  # 会阻塞

    print "i love you"

    request_message = connection.recv(4096)

    print 'request_message:'
    print request_message

    if request_message == local_request_message:

        connection.sendall(response.read().encode())

    else:

        connection.sendall('the message is the different'.encode())

# connection.close()
