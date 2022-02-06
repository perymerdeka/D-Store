from .base import *

# Installed Apps Settings
INSTALLED_APPS += [
    'accounts.apps.AccountsConfig',
    'dashboard.apps.DashboardConfig',
]

DEBUG = True

# Database Settings

DATABASES  = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
