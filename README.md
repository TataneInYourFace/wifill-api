# Wefill-API	

This is the rest API used by the [Wefill](https://github.com/TataneInYourFace/wefill) app.

## Summary

* [Prerequisites](#prerequisites)
* [Deploying](#deploying)
* [Provided URLs](#provided-urls)

## Prerequisites

Wefill-API uses [Python](https://www.python.org/downloads/) 2.7 / 3.5 / 3.6 coupled with [Django](https://www.djangoproject.com/download/) web framework.

We recommend using Python's packet manager, [pip](https://pypi.python.org/pypi/pip) to install packets :

```sh
pip install Django
```


The database depends on what you prefer. It can uses many DBMSs thanks to Django's [database management](https://docs.djangoproject.com/en/1.10/ref/databases/).

In addition to that, Wefill-API requires a bunch of python packets : 
```sh
pip install djangorestframework
pip install markdown # Markdown support for the browsable API.
pip install django-filter # Filtering support
pip install djangorestframework-jwt
pip install psycopg2 #used for PostegreSQL
pip install django-rest-swagger #api-doc
```

## Deploying

Last steps ! To avoid versionning sensible data such as secret keys or database informations, a `settings.py.dist` file has been created. Copy it in the same directory cutting the `.dist` extension to enable it. Fill it with your own informations.

Finally navigate to the project directory with your favorite CLI and create the database :
```sh
python manage.py migrate
```

That's it ! You can now start calling the API after launching the server : 
```sh
python manage.py runserver
```

## Provided urls

To call the API, your urls should start with : `http://127.0.0.1:8001/api/v1/`.

Note : Every request but `POST /users/` and `POST /login/` **must** provide the authentification token given by the API, with that very form :
```
Authorization: JWT exempleofjwttoken
```

Either registering or loging in will grant the user a token.

Browse `http://127.0.0.1:8000/api/docs/` to see a full list of callable urls.
