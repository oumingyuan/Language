#!/usr/bin/python
# coding=utf-8

import MySQLdb


def get_email():
    SELECT
    i.NAME, c.email, i.BIRTH, i.ID_CARD_NO
    FROM
    contact_information
    c
    INNER
    JOIN
    id_card
    i
    ON
    c.id_card_no = i.ID_CARD_NO

    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    cursor.execute(
        "SELECT i.NAME, c.email,i.BIRTH,i.ID_CARD_NO FROM contact_information c INNER JOIN id_card i ON c.id_card_no=i.ID_CARD_NO")

    results = cursor.fetchall()

    birthList = []
    emailList = []

    print "lala"

    for result in range(len(results)):
        tuple = results[result]

        birthList.append(tuple[2])
        emailList.append(tuple[1])

        print tuple[1]

    db.close()

    return emailList


get_email()
