"""
Django settings for faculty_management project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n!25(ar3a7+2d#r&y+kzjuw1+*l%8j*wua$kw-9vv=j74_*qe7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "faculty",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "faculty_management.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates",],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "faculty_management.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "verceldb",
        'USER': 'default',
        'PASSWORD': 'itreLEFl8IY4',
        'HOST': 'ep-shiny-fire-a1w9wrs9-pooler.ap-southeast-1.aws.neon.tech',
        'PORT': 5432,
    }
}
# POSTGRES_URL="postgres://default:itreLEFl8IY4@ep-shiny-fire-a1w9wrs9-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# POSTGRES_PRISMA_URL="postgres://default:itreLEFl8IY4@ep-shiny-fire-a1w9wrs9-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require&pgbouncer=true&connect_timeout=15"
# POSTGRES_URL_NO_SSL="postgres://default:itreLEFl8IY4@ep-shiny-fire-a1w9wrs9-pooler.ap-southeast-1.aws.neon.tech:5432/verceldb"
# POSTGRES_URL_NON_POOLING="postgres://default:itreLEFl8IY4@ep-shiny-fire-a1w9wrs9.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# POSTGRES_USER="default"
# POSTGRES_HOST="ep-shiny-fire-a1w9wrs9-pooler.ap-southeast-1.aws.neon.tech"
# POSTGRES_PASSWORD="itreLEFl8IY4"
# POSTGRES_DATABASE="verceldb"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# In your Django settings file (settings.py)
LOGIN_URL = '/faculty/login'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")