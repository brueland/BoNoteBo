# BoNoteBo

Data tracking application for Bonobo apes.

## Local Development

### Setup

This project depends on [Python](https://www.python.org/) and [NodeJS](https://nodejs.org/en).
You'll need to install both of those language runtimes on your local machine in order to run this application.

### Virtual Environment

If you are unfamiliar with [virtual environments](https://docs.python.org/3/library/venv.html), I suggest taking a brief moment to learn about them and set one up.
The Python docs provide a great [tutorial](https://docs.python.org/3/tutorial/venv.html) for getting started with virtual environments and packages.

This project's dependencies can be installed via pip:

```
pip install -r requirements.txt
```

### Migrations

First, prepare and apply any pending database migrations:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Admin User

Then, you'll probably want to create an admin user:

```
python3 manage.py createsuperuser
```

### Running

Lastly, run the site using the builtin web server:

```
python3 manage.py runserver
```
