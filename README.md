# Newspaper agency

System for tracking Redactors, assigned to Newspapers

## Check it out!
[Newspaper agency project deployed to Render](https://newspaper-project.onrender.com/)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/WonnaKoo/newspaper-agency.git
cd newspaper-agency
python3 -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver # starts Django server
```

## Features

* Authentication functionality for Redactor/User
* Managing newspaper redactors and titles directly from website interface
* Admin panel for advanced managing


## Test username & password

* Username: admin
* Password: test_password
