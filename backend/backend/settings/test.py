from .base import *  # noqa: F401,F403

DEBUG = True
SECRET_KEY = "test-only-secret-key-that-is-at-least-32-bytes"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

CORS_ALLOWED_ORIGINS = []
