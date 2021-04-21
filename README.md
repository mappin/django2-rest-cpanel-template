![Python](https://img.shields.io/badge/python-3.7.10-green.svg)
![Django](https://img.shields.io/badge/django-2.1.2-green.svg)
![Version](https://img.shields.io/badge/version-0.1.0-yellow.svg)
# django2-rest-cpanel-template
My custom Django template for Cpanel.  I will update with every Cpanel updates.

## Requirements
- Python 3.7.10 (or Anaconda Python for local development)
- Cpanel v94 (requires Select Python App)
- alt-python37 (CloudLinux)
- wsgi via Phusion Passenger
---
## Prerequisites
- A Web Hosting account (with Cpanel)
- Python Selector Application installed by hosting company

## Installation
1. Login in to Cpanel
2. Under Software, Select Python App, 
3. Click Create Application
4. Select Python version (e.g. 3.7.10)
5. Select Application root (e.g. Django2_py37), this will create a project folder and Python virtual environment
6. Select Domain
7. Leave Application startup file as blank (f you do not specify a startup file, cPanel creates a **passenger_wsgi.py** startup file for you.)
8. eave Application entry point as blank (f you do not specify the application entry point, cPanel creates a default **application** object for you.)
9. Optionally specify Passenger log file for the app (Logging is not supported on servers running LiteSpeed.)
10. Clone this repo using Cpanel git.

Refer [Cpanel Python Docs](https://docs.cpanel.net/knowledge-base/web-services/how-to-install-a-python-wsgi-application/) and [Cpanel Git Blog](https://blog.cpanel.com/git-version-control-series-what-is-git/) for additional information.

```bash
$ source /home/username/virtualenv/application/version/bin/activate && cd /home/username/application 
$ python
$ pip install --upgrade pip
$ pip install -r requirements/development.pip
```
If you change anything, please run `makemigrations` to keep track of your db.
Then continue to work:

```bash
$ python manage.py migrate
$ python manage.py createsuperuser

# enter: Email, First Name, Last Name and password (go to /admin to add more users)
$ python manage.py runserver
```

---

## Features
- Django application structure for Cpanel
- All Django apps live under `applications/` folder.
- All of the models live under generated app’s `models/` folder.
- All of the views live under generated app’s `views/` folder.
- All of the tests live under generated app’s `tests/` folder.
- All of the admin files live under generated app’s `admin/` folder.
- Every app should contain It’s own `urls.py`.
- All settings related files will live under `config/settings/` folder.
- Every environment has It’s own setting such as `config/settings/development.py`.
- Every environment/settings can have It’s own package/module requirements.
- All of the templates live under basedir’s `templates/APP_NAME` folder.
---

## Quick Start

You can fix your Django Admin titles now. Go to `config/urls.py` and fix:

```python
admin.site.index_title = _('Your admin index title')
admin.site.site_title = _('Your site title')
admin.site.site_header = _('Your site header')
```

Let’s create `api` application. 
First, create new appn:

```bash
$ python manage.py create_app api
```

Fix your `config/settings/base.py`, add this newly created app to your `INSTALLED_APPS`:

```python
# config/settings/base.py
:
:
AUTH_USER_MODEL = 'baseapp.User'

INSTALLED_APPS += [
    'api.apps.APIConfig',
]
```

Now, if you fix your `config/urls.py` you’ll be able to see demo
pages for your app:

```python
# config/urls.py
:
:
urlpatterns = [
    # ...
    path('api/', include('api.urls', namespace='api')),
    # ..
]
```

Now run server and call `http://127.0.0.1:8000/api/`:

```bash
$ python manage.py runserver
```

Let’s look at our `api` application structure:

```bash
    api/
    ├── admin
    │   └── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   └── index.py
    ├── views
    │   ├── __init__.py
    │   └── index.py
    ├── __init__.py
    ├── apps.py
    └── urls.py
```

Here is main directory/file structure:

```bash
.
├── baseapp
├── config
│   ├── settings
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── db
├── locale
│   └── eng
├── requirements
│   ├── base.pip
│   ├── development.pip
│   └── production.pip
├── static
│   └── css
├── templates
│   ├── admin
│   ├── baseapp
│   └── base.html
├── manage.py
└── requirements.txt
```

---

## Settings and Requirements Abstraction

By default, `manage.py` looks for `DJANGO_ENV` environment variable. Builds 
`DJANGO_SETTINGS_MODULE` environment variable according to `DJANGO_ENV` variable.
If your `DJANGO_ENV` environment variable is set to `production`, this means that
you are running `config/settings/production.py`.

Also `config/wsgi.py` looks for `DJANGO_ENV` environment variable too. 

All the other settings files (*according to environment*) imports
`config/settings/base.py` and gets everything from it. `development.py` is
un-tracked/git-ignored file. Original file is `development.example.py`. You
need to create a copy of it! (*if you follow along from the beginning, you’ve already did this*)

All the base/common required Python packages/modules are defined under `requirements/base.pip`:

```bash
Django==2.1.2
```