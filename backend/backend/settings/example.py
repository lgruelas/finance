# flake8: noqa

# THIS IS AN EXAMPLE OF HOW YOUR FILE SHOULD LOOKS LIKE

from backend.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_WHITELIST = (
    'your frontend url'
)
