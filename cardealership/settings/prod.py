from .base import *
import dj_database_url

SECRET_KEY = config("SECRET_KEY")

DATABASES= {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }