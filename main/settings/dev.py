"""
로컬 개발 환경 설정입니다.
"""
import os

from main.settings.base import *
import json

# DOCKER SETTING
"""
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

STATICFILES_DIRS = (
   os.path.join('main', 'static'),
)
"""

DEBUG = True

# 로컬 데이터베이스 설정을 해주시면 됩니다
CONFIG_DIR = os.path.join(BASE_DIR, '.config')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'common_settings.json')

config_load = json.loads(open(CONFIG_FILE).read())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_load['DB_NAME'],
        'USER' : config_load['DB_USER'],
        'PASSWORD' : config_load['DB_PASSWORD'],
        'HOST' : config_load['DB_HOST'],
        'PORT' : config_load['DB_PORT'],
    }
}

STATICFILES_DIRS = (
   os.path.join('main', 'static'),
)