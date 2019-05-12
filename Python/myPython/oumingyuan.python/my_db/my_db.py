import MySQLdb

db = MySQLdb.connect("rm-uf691aogdbexr1ltvo.mysql.rds.aliyuncs.com", "root", "yuan123/", "yue")

print db

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print data

db.close()
