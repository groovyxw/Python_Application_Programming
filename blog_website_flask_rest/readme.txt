- download the repo.
$ git clone URL

-go to project folder
$ cd flasky

-set virtual environment

$ python3 -m venv venv

-activate virt. environment

$ . venv/bin/activate

-install requirements and dependencies
$ pip install wheel
$ pip install -r requirements/prod.txt

-export environ. variable

$ export FLASK_APP=flasky.py
$ export MAIL_USERNAME=<email>
$ export MAIL_PASSWORD=<pwd>

-set database and migrations.

$ flask db stamp head
$ flask db migrate
$ flask db upgrade
- run app
$ flask run
- go to http://127.0.0.1:5000/
- register using email and pwd.
- exit the termimal

- open up 2nd terminal.
$ python3 -m flask deploy
$ python3 -m flask run

- open up 3rd terminal
$ sqlite3 data-dev.sqlite
- set your user as confirmed manually.
$ UPDATE users SET confirmed=1 WHERE id=1;
$ UPDATE users SET role_id=3 WHERE id=1;
$ exit;

Start using the app at http://127.0.0.1:5000
