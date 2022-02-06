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
        'NAME': 'd405vd3or6dahc',
        'USER': 'opinlszxzbjbss',
        'PASSWORD': '924318280b3bb1bd626537181ab2ee8e6bbdd7ea337c46a54cc6318f8eaf33de',
        'HOST': 'ec2-54-164-56-10.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}