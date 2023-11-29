import os
from .settings import *
import mysql.connector
from mysql.connector import errorcode
#from devsecrets import secrets




SECRET_KEY = os.environ['SECRET'] #jos devsecrets käyttöön otetaan ni vaihtaa SECRET_KEYksi.
ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] #muutettu tätä ja debug laitettu päälle joten nyt voi nähdä livestä virheilmoitukset https://palautekooderit-project.azurewebsites.net/
DEBUG = True


# This should be added when in Azure environment?
#INSTALLED_APPS.append("palautekooderit.apps.AzureContentConfig")
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
        'HOST': conn_str_params['Server'],
        'NAME': conn_str_params['Database'],
        'PORT': conn_str_params['Port'],
        'USER': conn_str_params['User Id'],
        'PASSWORD': os.environ['AZURE_MYSQL_PASSWORD'] #ei välttämättä toimi jne. Ei välttis pitäiskään. Pitää saada mysql autentikoitumaan salasanan kanssa.
    }
}
"""
db_user = secrets.get('DATABASE_USER', 'root') 
db_pass = secrets.get('DATABASE_PASSWORD', 'pass') 
db_port = secrets.get('DATABASE_PORT', 3306) 
  
cnx = mysql.connector.connect(user="db_user", password="db_pass", host="palautekooderit-project-server.mysql.database.azure.com", port=3306, database="palautekooderit-project-database", ssl_ca="", ssl_disabled=True)

try:
  cnx = mysql.connector.connect(user='db_user',
                                database='palautekooderit-project-database')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
  """