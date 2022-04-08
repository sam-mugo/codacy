# codacy
- A tutorial aggregator site made using Django

- clone or download the repo; then
follow the instructions below

```
$ cd codacy
## create and use a python virtualenv:

$py3 -m venv codacyvenv
$../codacyvenv/scripts/activate

## install all dependencies

$ pip install -r requirements.txt

## database priming and schema creation
$ py manage.py makemigrations
$ py manage.py migrate

## create a superuser
$ py manage.py createsuperuser

## Run the application
$ py manage.py runserver
Load http://127.0.0.1:8000/ in your browser.

## How to contribute
1. I am currently in the process of phasing out Bulma-Css for bootstrap4 as this is the version supported by crispy forms.

2. The accounts system- authentication (login,signup, change-password) are not styled and this is of high priority right now
