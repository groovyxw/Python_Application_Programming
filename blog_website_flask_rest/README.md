# Blog_website_flask_rest

## Description:
Use flask and REST to implement a blog website. It support registration&confirmation, post blog, eidt profile and write comments, follow functions.


## How to run it?

- download the repo.
> $ git clone url

- go to project folder
> $ cd flasky

- set virtual environment

> $ python3 -m venv venv

- activate virt. environment

> $ . venv/bin/activate

- install requirements and dependencies
> $pip install wheel

> $ pip install -r requirements/prod.txt

- export environ. variable

> $ export FLASK_APP=flasky.py

> $ export MAIL_USERNAME=<EMAIL>
  
> $ export MAIL_PASSWARD=<PWD>

- set database and migrations.

> $ flask db stamp head
  
> $ flask db migrate
  
> $ flask db upgrade
  
- run app
> $ flask run
  
- go to http://127.0.0.1:5000/
- register using email and pwd.  
  
- go back to the terminal.
> $python3 -m flask deploy
  
> $python3 -m flask run
  
- open 2nd terminal
> $ sqlite3 data-dev.sqlite
  
- set your user as confirmed manually.
> $ UPDATE users SET confirmed=1 WHERE id=1;
  
> $ UPDATE users SET role_id=3 WHERE id=1;
> $ exit;
  
Start using the app at > http://127.0.0.1:5000
  
![GitHub Logo](imgs/Flask_test_9.PNG)

![GitHub Logo](imgs/post_test_9.PNG)


## Presentation:
https://docs.google.com/presentation/d/1A2jTm-GPnWeuwUY8zLOlER_K-cSbubWWZ91jEkI8Zw0/edit#slide=id.p
