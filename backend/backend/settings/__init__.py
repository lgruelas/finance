# flake8: noqa
import os
if "DJANGO_DEBUG_DOCKER" in os.environ:
    from .dev import *
elif "DJANGO_DEBUG_LOCAL" in os.environ:
    from .local import *