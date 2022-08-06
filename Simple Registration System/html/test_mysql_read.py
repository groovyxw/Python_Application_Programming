#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","test123","cs531" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM tb1 \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      uid = row[0]
      uname = row[1]
      uemail = row[2]
      udate = row[3]
      # Now print fetched result
      print ("uid = %d,uname = %s,uemail = %d,udate = %s" % \
             (uid, uname, uemail, udate))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()
    
