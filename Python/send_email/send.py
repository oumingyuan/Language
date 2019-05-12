from ming.my_db import email_info
import time
from ming.my_email import new_email

db_info = email_info.get_log_info()

for element in db_info:
    print(element)

    information = '您好，我是你们的小萌主，祝你周末快乐。您本周的日志内容如下：\n' + str(
        element[3]) + '\n如果有问题请您在今天晚上11点之前修改。日志填写地址：http://120.79.223.29:8081/log/login.html，请用IE或360浏览器。'

    print(information)

    print(element[4])

    new_email.send_email(element[4], element[2], information)

    time.sleep(10)
