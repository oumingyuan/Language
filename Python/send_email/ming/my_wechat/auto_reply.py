import itchat
import sys


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


if 'win32' == sys.platform:
    itchat.auto_login()
else:
    itchat.auto_login(enableCmdQR=2)

itchat.run()
