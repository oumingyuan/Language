#!/usr/bin/python
# coding=utf-8


from . import my_db


def get_information():
    db = my_db.get_db_local()

    cursor = db.cursor()
    sql = 'SELECT i.NAME, c.email,i.BIRTH,i.ID_CARD_NO FROM ou.contact_information c INNER JOIN ou.id_card i ON c.id_card_no=i.ID_CARD_NO'

    cursor.execute(sql)

    results = cursor.fetchall()

    return results


def get_log_info():
    db = my_db.get_db_local()

    cursor = db.cursor()

    sql = 'SELECT * FROM `company_log`.`user_info` LIMIT 0, 1000'

    cursor.execute(sql)

    return cursor.fetchall()


all_login_data = (

    {'code': 'mingyuan.ou', 'password': '/yuan15555136971'},
    {'code': 'guobing.wang', 'password': 'wanggb2018@'},

)
