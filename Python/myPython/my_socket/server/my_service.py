#!/usr/bin/python
# coding=utf-8

import socket

# socket 的初始化
HOST = '192.168.0.110'
PORT = 8888

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(10)

connection, address = socket.accept()

# 服务器判断逻辑
local_request = open('request.txt')
local_request_message = local_request.read()

request_message = connection.recv(1024)

response = open('response.txt')

if request_message == local_request_message:

    connection.sendall(response.read().encode())

else:

    connection.sendall('the message is the different'.encode())

connection.close()
