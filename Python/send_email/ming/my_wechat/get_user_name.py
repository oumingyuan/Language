# coding=utf8
import itchat

itchat.auto_login(hotReload=True)

# 想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
users = itchat.search_friends(name='汪国兵')
# 获取好友全部信息,返回一个列表,列表内是一个字典
print(users)
# 获取`UserName`,用于发送消息
userName = users[0]['UserName']
itchat.send("路上小心", toUserName=userName)
