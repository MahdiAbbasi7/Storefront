from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-e6n(603gj-%f^_%^opggn^xyxus@-d@zk=w7jix1)@9l=hlc#$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront2',
        'HOST': 'localhost',
        'USER': 'mahdi',
        'PASSWORD': '1',
    }
}
