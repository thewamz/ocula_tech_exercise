import os

from .base import *  # noqa

ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")

SECRET_KEY = os.environ["SECRET_KEY"]  # noqa
DEBUG = False
