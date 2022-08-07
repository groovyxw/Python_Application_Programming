#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","xin","cs531" )
print("Connected to Database successfully!")

# prepare a cursor object using cursor() method
cur = db.cursor()

#sql = "SELECT * FROM tb1"
try:
   # Execute the SQL command
   # Select query
    cur.execute("select * from tb1")
    output = cur.fetchall()
    print(output)  
    for row in output:
      #uid = row[0]
      uname = row[0]
      uemail = row[1]
      # Now print fetched result
      #print ("uid = %d,uname = %s,uemail = %d,udate = %s" % \
      print ("uname = %s,uemail = %s" % \
             (uname, uemail))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()
