from .base import *  # noqa

ENVIRONMENT = "docker"

SECRET_KEY = os.environ.get(  # noqa
    "SECRET_KEY", "django-insecure-vl^_nz@5hn&ndtzburh_)zpj56-(x%na8mjm)u1p6tjx-39p!m"
)
DEBUG = bool(int(os.environ.get("DEBUG", 1)))  # noqa
