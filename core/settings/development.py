from .base import *

# Installed Apps Settings
INSTALLED_APPS += [
    "accounts.apps.AccountsConfig",
    "dashboard.apps.DashboardConfig",
]

DEBUG = True

# Database Settings

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# SMTP Configurations
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "tkjasikk@gmail.com"
EMAIL_HOST_PASSWORD = "sempakuda"
