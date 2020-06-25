from core.base import *
import configparser

DEBUG = False
ALLOWED_HOSTS = ['*']


SECRET_KEY = os.environ.get("djangoSecKey")

# read conf file
CAPTCHA_PRIVATE = os.environ.get("captcha_private")
CAPTCHA_PUBLIC = os.environ.get("captcha_public")

DATABASEENGINE = os.environ.get("ENGINE")
DATABASENAME = os.environ.get("POSTGRES_DB")
DATABASEUSER = os.environ.get("POSTGRES_USER")
DATABASEPWD = os.environ.get("POSTGRES_PASSWORD")
DATABASEHOST = os.environ.get("HOST")
DATABASEPORT = os.environ.get("POSTGRES_PORT")

DATABASES = {
    'default': {
        'ENGINE': DATABASEENGINE,
        'NAME': DATABASENAME,
        'USER': DATABASEUSER,
        'PASSWORD': DATABASEPWD,
        'HOST': DATABASEHOST,
        'PORT': DATABASEPORT,
    }
}

print('from the dev profile the secret key = ', SECRET_KEY)
