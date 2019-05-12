import MySQLdb
import time
from email import my_email

db = MySQLdb.connect("rm-uf691aogdbexr1ltvo.mysql.rds.aliyuncs.com", "root", "yuan123/", "yue", charset="utf8")

cursor = db.cursor()

cursor.execute("SELECT id_card.ID_CARD_NO, id_card.BIRTH FROM id_card")

results = cursor.fetchall()

print type(results)

print results

for row in results:

    time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    if time_now[5:10] == row[1][5:10]:

        print "send email"

        cursor.execute("SELECT contact_information.email FROM contact_information")

        email_results = cursor.fetchall()

        print email_results

        for email_list in email_results:
            email = email_list[0]

            print email

            my_email.send_email(email)

db.close()
