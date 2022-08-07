#!/usr/bin/python3

import cgi, cgitb
import pymysql
import smtplib

#send SMS through email
def sendEmail(uname, uemail):
    # store gmail password in my google drive (not the most secure way)
    # but it is much safer than storing it directly in this notebook,
    # and upload it to github for everyone to see
    ##with open('/content/gdrive/My Drive/Colab Notebooks/pw.txt') as file:
    #    data = file.readlines()
    #gmail_password = data[0]
 
    gmail_user = 'cindy20160105@gmail.com'
    gmail_password = 'cyaqaymzfdtjjbob'

    sent_from = gmail_user
    to = [uemail]
    subject = 'Shopping Cart System'
    body = '%s\n\n- Thank you for the registration!' % uname

    email_text = \
"""From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.quit()

    #print(f'Email: \n{email_text}')


#insert user information into database
def insertRecord(uname, uemail):
    status = False
    # Open database connection
    db = pymysql.connect("localhost","root","xin","cs531" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
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
       status = True
    except:
       # Rollback in case there is any error
       print("Error: Insert failed!")
       db.rollback()
    
    # disconnect from server
    db.close()
    return status


#read user information from database
def readRecord():
    # Open database connection
    db = pymysql.connect("localhost","root","xin","cs531" )
    #print("Connected to Database successfully!")
    
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    uname = None
    uemail = None

    try:
       # Execute the SQL command -- select query
        cur.execute("select * from tb1")
        output = cur.fetchall()
        #print(len(output), output)
        
        #fectch the last record
        if len(output) > 0:  
             uname = output[len(output)-1][0]
             uemail = output[len(output)-1][1]

          # Now print fetched result
          #print ("uname = %s,uemail = %s" % \
          #       (uname, uemail))
    except:
       print ("Error: unable to fetch data")
    
    # disconnect from server
    db.close()
    return uname,uemail


def main():    
    ## Import modules for CGI handling
    cgitb.enable()
    # Create instance of FieldStorage
    form = cgi.FieldStorage()
    ## Get data from fields
    confirm = form.getvalue('confirm')
    uemail = form.getvalue('email')
    uname = form.getvalue('name')
    
    print("Content-type:text/html\r\n\r\n")
    print("<HTML>")
    print("<HEAD>")
    print("<TITLE>Confirmation REACTION</TITLE>")
    print("</HEAD>")
    print("<BODY>")
    print("")
    if confirm == "no":
        print("<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >")
        print("<TR VALIGN=TOP>")
        print("<TD>")
        print("<pre>")
        print('So, The Information Is Incorrect.')
        print('       <a href="/cgi-bin/regist.py">Please Registration Again</a>')
        print('       <a href="../regist.html">Back To Top</a>')
        print("</pre>")
        print("</TD>")
        print("</TR>")
        print("</TABLE>")
    elif confirm == 'yes':
        success = insertRecord(uname, uemail)
        if success:
            (uname,uemail) = readRecord()
            if uname is not None and uemail is not None:
                #print(uname, uemail)
                sendEmail(uname, uemail)

        #display html
        print("<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >")
        print("<TR VALIGN=TOP>")
        print("<TD>")
        print("<pre>")
        print("Registration Successful")
        print("")
        print("     Thanks")
        print("</pre>")
        print("</TD>")
        print("</TR>")
        print("")
        print("</TABLE>")
    print("</BODY>")
    print("</HTML>")
    

main()
