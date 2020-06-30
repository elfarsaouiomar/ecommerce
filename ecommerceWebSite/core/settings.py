import os
from oscar.defaults import *
import environ
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weShop',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_jenkins', # django-jenkins test

    'oscar',
    'oscar.apps.analytics',
    'oscar.apps.checkout',
    'oscar.apps.address',
    'oscar.apps.shipping',
    'oscar.apps.catalogue',
    'oscar.apps.catalogue.reviews',
    'oscar.apps.partner',
    'oscar.apps.basket',
    'oscar.apps.payment',
    'oscar.apps.offer',
    'oscar.apps.order',
    'oscar.apps.customer',
    'oscar.apps.search',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'oscar.apps.dashboard',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.orders',
    'oscar.apps.dashboard.catalogue',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.vouchers',
    'oscar.apps.dashboard.communications',
    'oscar.apps.dashboard.shipping',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_pylint',
    #'django_jenkins.tasks.run_jslint',
    #'django_jenkins.tasks.run_csslint',
    #'django_jenkins.tasks.run_sloccount'
)

SITE_ID = 1

DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]
SECRET_KEY = os.environ.get("djangoSecKey")


# read conf file
CAPTCHA_PRIVATE = os.environ.get("captcha_private")
CAPTCHA_PUBLIC = os.environ.get("captcha_public")

DATABASENAME = os.environ.get("POSTGRES_DB")
DATABASEUSER = os.environ.get("POSTGRES_USER")
DATABASEPWD = os.environ.get("POSTGRES_PASSWORD")
DATABASEHOST = os.environ.get("HOST")
DATABASEPORT = os.environ.get("POSTGRES_PORT")

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
  
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
MEDIA_URL = '/upload/'



