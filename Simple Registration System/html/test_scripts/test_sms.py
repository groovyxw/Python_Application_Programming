#!/usr/bin/python3

import smtplib

def SendEmail(uname, uemail):
    # store gmail password in my google drive (not the most secure way)
    # but it is much safer than storing it directly in this notebook,
    # and upload it to github for everyone to see
    ##with open('/content/gdrive/My Drive/Colab Notebooks/pw.txt') as file:
    #    data = file.readlines()
    #gmail_password = data[0]
 
    gmail_user = 'cindy2016@gmail.com'
    gmail_password = 'cccyaqaymzfdtjjbob'

    sent_from = gmail_user
    to = [uemail]
    subject = 'Shopping Cart System'
    body = '%s\n\n- Thank you' % uname

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

    print(f'Email: \n{email_text}')

uname = 'cindy'
uemail = 'cindy@student.sfbu.edu'
SendEmail(uname, uemail)
