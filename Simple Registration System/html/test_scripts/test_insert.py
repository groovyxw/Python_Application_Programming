#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","cs531" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

uname = 'Mike'
uemail = 'mike@gmail.com'
# Prepare SQL query to INSERT a record into the database.
#sql = "INSERT INTO tb1(user_name, \
#   user_email) \
#   VALUES ('%s', '%s')" % \
#   ('Mac', 'Mohan@gmail.com')
sql = "INSERT INTO tb1(user_name, \
   user_email) \
   VALUES ('%s', '%s')" % \
   (uname, uemail)

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   print("Error: Insert failed!")
   db.rollback()

# disconnect from server
db.close()

