# flake8: noqa

# THIS IS AN EXAMPLE OF HOW YOUR FILE SHOULD LOOKS LIKE

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'finance',
        'USER': 'django_user',
        'PASSWORD': 'dockerpassword',
        'HOST': 'db',
        'PORT': '5432'
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)

INSTALLED_APPS = INSTALLED_APPS + [
    'django_extensions',
]

MEDIA_URL = '/static_media/media/'
MEDIA_ROOT = 'static_media/media/'
