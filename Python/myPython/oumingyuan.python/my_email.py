import smtplib
#from email.mime.text import MIMEText

from email.MIMEText import MIMEText
from email.Header import Header


# the method used to send email to someone
def send_email(address_of_receive):

    # the information of the service
    address_of_send = "709336535@qq.com"
    password_of_send = "ysuogvnurqdgbegd"

    # the detail of the email
    msg = MIMEText("test email and not to answer me")
    msg["Subject"] = "one hour one letter"
    msg["From"] = address_of_send
    msg["To"] = address_of_receive

    s = smtplib.SMTP_SSL("smtp.qq.com", 465)

    s.login(address_of_send, password_of_send)
    s.sendmail(address_of_send, address_of_receive, msg.as_string())
    s.quit()

    print "send email success"


send_email("281095871@qq.com")
