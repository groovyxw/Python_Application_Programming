#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
# Get data from fields
name = form.getvalue('name')
email  = form.getvalue('email')
print("""
<HTML>

<center><font color="black" size ="5">Registration Form</font><br>

<table align=center datasrc="#xmlRegData" border=2>
<tr><td><font color="black" size="5">Name:</font></td>""")
print("<td>%s </td> " %(name))
print("""</tr><tr><td><font color="black" size="5">Email:</font></td>""")
print(" <td>%s</td>" % (email))
print("""</tr>
</table><br>
<font size="5">Is this information correct ?</font>
<form action="/cgi-bin/confirm.py" method=GET>
<input type="hidden" id="name" name="name" value="%s">
<input type="hidden" id="email" name="email" value="%s">
Yes<input type=radio value="yes" name=confirm>
No<input type=radio value="no" name=confirm>  
<input type=submit value=Submit name=B1>        
<input type=reset value=Reset name=B2>
</form>
</center>
</html>""" % (name,email))
