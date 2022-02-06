# Heroku Settings

from .base import *

ALLOWED_HOSTS = ['dstore-django.herokuapp.com']

INSTALLED_APPS += [
    'accounts.apps.AccountsConfig',
    'dashboard.apps.DashboardConfig',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2pa8r8sk66a4t',
        'USER': 'gllfoqwzfpghdu',
        'PASSWORD': 'bb0b94ff14a652403b838b11cbac773484970c13a94be68d03c791b524bb9421',
        'HOST': 'ec2-54-157-15-228.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}