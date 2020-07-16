from .settings import *
from os import environ

DEBUG = environ.get("DEBUG")
ALLOWED_HOSTS = [environ.get("ALLOWED_HOSTS")]
SECRET_KEY = environ.get("djangoSecKey")


DATABASENAME = environ.get("POSTGRES_DB")
DATABASEUSER = environ.get("POSTGRES_USER")
DATABASEPWD = environ.get("POSTGRES_PASSWORD")
DATABASEHOST = environ.get("HOST")
DATABASEPORT = environ.get("POSTGRES_PORT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASENAME,
        'USER': DATABASEUSER,
        'PASSWORD': DATABASEPWD,
        'HOST': DATABASEHOST,
        'PORT': DATABASEPORT,
    }
}

