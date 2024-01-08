from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-e6n(603gj-%f^_%^opggn^xyxus@-d@zk=w7jix1)@9l=hlc#$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront2',
        'HOST': 'srv-captain--mariadb',
        'USER': 'root',
        'PASSWORD': '1',
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
