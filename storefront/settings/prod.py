import os
# import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["www.alihaddadi.sadrazkh.ir","193.164.4.226"]

# DATABASES = {
#     'default': dj_database_url.config()
# }
