# pylint: disable=W0401

#import dj_database_url

from .base import *  # noqa pylint: disable=E0401

#DATABASES = {'default': dj_database_url.config()}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
