# codacy
- A tutorial aggregator site made using Django



follow the instructions below to clone or download the repo; then


## create and use a python virtualenv:
```
$ cd codacy

$py3 -m venv codacyvenv
$../codacyvenv/scripts/activate
```

## install all dependencies
```
$ pip install -r requirements.txt
```

## database priming and schema creation
```
$ py manage.py makemigrations
$ py manage.py migrate
```

## create a superuser
```
$ py manage.py createsuperuser
```

## Run the application
```
$ py manage.py runserver
Load http://127.0.0.1:8000/ in your browser.
```

## How to contribute
```
1. I am currently in the process of phasing out Bulma-Css for bootstrap4 as this is the version supported by crispy forms.

2. The accounts system- authentication (login,signup, change-password) are not styled and this is of high priority right now

3. Add email and social account(github/google) registration
```

## MVP Features
```
- tutorials page ✔
- user registration ✔ (no email registration yet)
- Popular programming newletters
- user profile page
- upvote and downvote
- tutorial comments
- Programming tools
```

## Advanced features
```
- Programming languages Community leaders
- Ability for leaders to add tutorial content
- Tutorial detail (not just linking to external sites)
- Jobs and Scholarships
- Interview experiences
- Tech Salaries similar to levels.fyi
- Youtube Channel
```


