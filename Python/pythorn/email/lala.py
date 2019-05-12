import smtplib
from email.mime.text import MIMEText

address_of_send = "709336535@qq.com"
password_of_send = "ysuogvnurqdgbegd"
address_of_receive = "281095871@qq.com"

msg = MIMEText("速来开黑")
msg["Subject"] = "don't panic"
msg["From"] = address_of_send
msg["To"] = address_of_receive

s = smtplib.SMTP_SSL("smtp.qq.com", 465)

s.login(address_of_send, password_of_send)

s.sendmail(address_of_send, address_of_receive, msg.as_string())

s.quit()
# print("Success!")
