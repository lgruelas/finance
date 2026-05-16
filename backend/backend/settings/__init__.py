import os

if "DJANGO_DEBUG_DOCKER" in os.environ:
    from .dev import *  # noqa: F401,F403
elif "DJANGO_DEBUG_LOCAL" in os.environ:
    from .dev import *  # noqa: F401,F403
elif "DJANGO_PRODUCTION" in os.environ:
    from .prod import *  # noqa: F401,F403
