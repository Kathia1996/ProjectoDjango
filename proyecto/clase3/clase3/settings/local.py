from .base import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'clase3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : 'CursoDjango',
        'USER'      : 'root',
        'PASSWORD'  : '123',
        'HOST'      : 'localhost',
        'PORT'      : '5432'
        
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [BASE_DIR.child('static')]
