import socket

localIP = socket.gethostbyname(socket.gethostname())  # get local ip
print localIP

ipList = socket.gethostbyname_ex(socket.gethostname())


print ipList
