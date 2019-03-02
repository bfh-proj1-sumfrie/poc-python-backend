#!/usr/bin/python
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sqlquery-poc',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM user_details"
        cursor.execute(sql)
        for entry in cursor.fetchall():
            print(entry)
finally:
    connection.close()