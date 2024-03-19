# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-71e#1pt4g)c4mq5o-)x4b%s50s3ise9sqaho7&2h4z3gz&2v8r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


WSGI_APPLICATION = "budgeting_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
