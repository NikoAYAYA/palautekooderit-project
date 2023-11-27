import os
from .settings import *


SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = ['20.79.107.2']
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

# This should be added when in Azure environment?
INSTALLED_APPS.append("palautekooderit.apps.AzureContentConfig")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

conn_str = os.environ['AZURE_MYSQL_CONNECTIONSTRING']

pairs = conn_str.split(';')
conn_str_params = {}
for pair in pairs:
    if pair == "": continue

    p = pair.split('=')
    key = p[0]
    val = p[1]
    conn_str_params[key] = val

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
        # 'PORT': conn_str_params['3306']
    }
}
