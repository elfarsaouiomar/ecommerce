from .settings import *
from os import environ

DEBUG = environ.get("DEBUG")
ALLOWED_HOSTS = [environ.get("ALLOWED_HOSTS")]
SECRET_KEY = environ.get("djangoSecKey")

DATABASENAME = environ.get("POSTGRES_DB_TEST")
DATABASEUSER = environ.get("POSTGRES_USER_TEST")
DATABASEPWD = environ.get("POSTGRES_PASSWORD_TEST")
DATABASEHOST = environ.get("HOST_TEST")
DATABASEPORT = environ.get("POSTGRES_PORT_TEST")



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

