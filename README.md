# BoNoteBo

Data tracking application for Bonobo apes.

## Local Development

### Setup

This project depends on [Python](https://www.python.org/) and [NodeJS](https://nodejs.org/en).
You'll need to install both of those language runtimes on your local machine in order to run this application.

### Dependencies

If you are unfamiliar with [virtual environments](https://docs.python.org/3/library/venv.html), I suggest taking a brief moment to learn about them and set one up.
The Python docs provide a great [tutorial](https://docs.python.org/3/tutorial/venv.html) for getting started with virtual environments and packages.

This project's dependencies can be installed via pip:

```
pip install -r requirements.txt
```

You'll also want to install [Django-Tailwind's](https://django-tailwind.readthedocs.io/en/latest/installation.html) dependencies via:

```
python3 manage.py tailwind install
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

Lastly, run the site's [tailwindcss](https://tailwindcss.com/) watcher in one terminal:

```
python3 manage.py tailwind start
```

and run the site's builtin web server in another:

```
python3 manage.py runserver
```

### Formatting

To format the code, run [Black](https://github.com/psf/black) to format the Python files and [djLint](https://www.djlint.com/) to format the HTML templates:

```
black .
djlint . --reformat
```

## Requirements

This section describes everything that this application is supposed to do.
It outlines the user roles and the "stories" of the actions they'll take.

### User Roles

1. Admin - Individuals that administer the site (like Wes or Andrew)
   1. Can do everything an Admin, Manager, or Employee can do
2. Manager / Leader - Individuals in charge of operations and managing the facility and its employees
   1. Can do everything a Manager or Employee can do
3. Employee / Worker / Volunteer - Individuals who work at the facility and help take care of the animals (feed, observe)
   1. Can only perform permitted Employee tasks

### User Stories

This section describes each and every task that a user of the application can perform.
They are loosely grouped by frequency to help design the app in such a way that user are naturally guided toward common actions.

#### High Frequency

- Employee logs into the application
- Employee logs out of the application
- Employee resets their password
  - Can this thing send emails?
- Employee feeds one or more apes
  - What food item?
  - How much of it?
    - If feeding multiple, how does the quantity work? Split or each?
  - At what time? (default to now but allow fixing)
- Employee observes information about an ape
  - Weight
  - Swelling
  - Stool
  - Status
  - Time (default to now but allow fixing)
- Employee updates an existing observation
- Employee deletes an existing observation (who can do this?)

#### Medium Frequency

- Employee adds a new food item
  - Icon
  - Unit (what is a serving)
  - Calories per unit
- Employee updates an existing food item
- Manager creates various reports about ape info (TODO: needs context)
  - Info will likely be per-ape
  - Including info about diet and health
  - Likely over a period of time?

#### Low Frequency

- Manager adds a new Manager / Employee to the system
- Manager deletes an existing Employee to the system
  - Can they delete other Managers?
- Manager adds a new ape
- Manager archives an existing ape
  - Don't delete them: keep the historical data around
