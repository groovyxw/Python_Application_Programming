#!/usr/bin/python3

## Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
## Get data from fields
confirm = form.getvalue('confirm')

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
else:
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
