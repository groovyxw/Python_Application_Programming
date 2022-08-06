import smtplib

def SendEmail(msg):
    # store gmail password in my google drive (not the most secure way)
    # but it is much safer than storing it directly in this notebook, 
    # and upload it to github for everyone to see
    with open('/content/drive/MyDrive/Colab\ Notebooks/pw.txt') as file:
    #with open('/content/gdrive/My Drive/Colab Notebooks/pw.txt') as file:
        data = file.readlines()
        
    gmail_user = 'cindy2016@gmail.com'  
    gmail_password = data[0]

    sent_from = gmail_user  
    to = ['cindybayarea22@gmail.com']  
    subject = msg  
    body = '%s\n\n- Thank you' % msg

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
