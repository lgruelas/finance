from .base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = "dev-only-secret-key-change-me"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "finance",
        "USER": "django_user",
        "PASSWORD": "dockerpassword",
        "HOST": "db",
        "PORT": "5432",
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

INSTALLED_APPS = INSTALLED_APPS + [  # noqa: F405
    "django_extensions",
]
