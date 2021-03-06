"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p860h$3n$c%dz!z!al5rr9-3!%elg7vs(zgh4!6-v)!2$%6w+y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'sign',
    'protect',
    'appointments.apps.AppointmentConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
    'mcdonalds',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_L10N = True

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / "news/static"]

# LOGIN_URL = '/sign/login/'

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/news/'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}
#???????????????????? ?????????????????? (??????????????) ?? ????????????????????, ?????????? ???????????? ???????????????????????? ???? ???? ???????????????? ????????????, ?? ?????? ?? ??????????
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'st3p.pavel@yandex.ru'
EMAIL_HOST = 'smtp.yandex.ru'  # ?????????? ?????????????? ????????????-?????????? ?????? ???????? ???????? ?? ?????? ????
EMAIL_PORT = 465  # ???????? smtp ?????????????? ???????? ????????????????????
EMAIL_HOST_USER = 'st3p.pavel'  # ???????? ?????? ????????????????????????, ????????????????, ???????? ???????? ?????????? user@yandex.ru,
# ???? ???????? ???????? ???????????? user, ?????????? ??????????????, ?????? ?????? ???? ?????? ???????? ???? ????????????
EMAIL_HOST_PASSWORD = '3Dr4V67VY1IT'  # ???????????? ???? ??????????
EMAIL_USE_SSL = True  # ???????????? ???????????????????? ssl, ?????????????????? ?? ??????, ?????? ??????, ?????????????????? ?? ???????????????????????????? ????????????????????,
# ???? ???????????????? ?????? ?????????? ??????????????????????

# ???????????? ???????? ??????????????, ?????????????????? ?? ?????????????? ('??????', '???? ??????????' (?? ???????? ???????????? ???? ?????????????????????? ???????????? ?????????????????????? ?? ????????????(????????))
ADMINS = [
    ('Mail', 'stepa.hax@bk.ru'),

    ('Yandex', 'st3p.pavel@yandex.ru'),

]

MANAGERS = [
    ('Mail', 'stepanov.hax@bk.ru'),
    ('Yandex', 'st3p.pavel@yandex.ru')
]

SERVER_EMAIL = 'st3p.pavel@yandex.ru'  # ?????? ?????????? ?? ?????? ???????????? ?????????????????? FROM ?? ???????????????? ????????????????
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

# Celery,Redis
# ?????????????????? ???? URL ?????????????? ?????????????????? (Redis). ???? ?????????????????? ???? ?????????????????? ???? ?????????? 6379
# ???????? ?????????????????? ???????????????????? ???????????? ?????? ?????????? ??????????
# ???????????????? ?????? (???? ????????)
# CELERY_BROKER_URL = 'redis://localhost:6379'
# ???? ???????????? ??????????????
# redis://:password@hostname:port/db_number
# db_number = 0, ??????????????????????, ?????????? ???????????? ??????????
# ???? ??????
CELERY_BROKER_URL = 'redis://:SQgQovYVrRQ85HmXfcqtVYH6wmdhSUar@redis-14226.c51.ap-southeast-2-1.ec2.cloud.redislabs.com:14226/0'

# ???????? ?????????? ???????????????????????? ?????? ????????????, ?????????????????? ???? ?????????????????? ?????????????????????? ???????????????????? ??????????
# ???????????????? ??????
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# ???? ??????
CELERY_RESULT_BACKEND = 'redis://:SQgQovYVrRQ85HmXfcqtVYH6wmdhSUar@redis-14226.c51.ap-southeast-2-1.ec2.cloud.redislabs.com:14226/0'
# ???????????? ?????????? ????????????
CELERY_ACCEPT_CONTENT = ['application/json']
# ???????????? ????????????, ?????????? ???????????????????????? ??????????
CELERY_TASK_SERIALIZER = 'json'
# ???????????? ????????????, ?????????? ???????????????????????? ??????????????????????
CELERY_RESULT_SERIALIZER = 'json'