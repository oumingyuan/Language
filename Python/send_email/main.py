from ming.my_db import email_info

db_info = email_info.get_information()

for element in db_info:

    print(element)
