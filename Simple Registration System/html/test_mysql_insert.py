#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","test123","cs531" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO tb1(
   user_name, user_email, user_submission_date)
   VALUES ('cindy', 'cindybayarea@gmail.com', '08/06/2022')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

# disconnect from server
db.close()
