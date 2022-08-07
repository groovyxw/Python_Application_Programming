# Simple registration system using CGI API

## Description
Implement a simple registration system. 
1. Main website page with "Start register" click button.
2. "Register form" page, used for user to enter their personal information
3. Process the personal information and let user to confirm the correctness of it.
4. If confirmation is ok, show "sucessful" page; otherwise back to main page or registration form page.
5. Support use public 


## Code Structure


![GitHub Logo](imgs/dir_structure.PNG)


## How to run it?

Platform: Windows WSL ubuntu

-download code
   > $ git clone url
    
-enter html directory
   > $ cd html

-start the web server
   > $ python3 -m http.server --cgi
    
-open the website on browser, e.g. Chrome
   > http://localhost:8000/regist.html
    
-Register according to the web page
(Reference screenshots are attached below)


![GitHub Logo](imgs/welcomepage.PNG)

![GitHub Logo](imgs/regpage.PNG)

![GitHub Logo](imgs/confirmation_center.PNG)

![GitHub Logo](imgs/test_3.PNG)

![GitHub Logo](imgs/test_2.PNG)


# Presentation: 
https://docs.google.com/presentation/d/1FyIrlJA3WTnbzaDEfuleL5Q8c7wE7_NfK12bjw21T9o/edit?usp=sharing
