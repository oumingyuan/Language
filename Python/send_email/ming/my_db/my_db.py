#!/usr/bin/python
# coding=utf-8

import pymysql
import sys

'''本地mysql 服务器'''


def get_db_local():
    # host = "rm-uf64d5uetcz154o74o.mysql.rds.aliyuncs.com"

    host = "localhost"

    if 'win32' == sys.platform:
        password = "123456"
    else:
        password = "new_password"

    user = "root"

    database = "company_log"

    db = pymysql.connect(host, user, password, database, charset="utf8")

    return db
