from .base import *
import dj_database_url

SECRET_KEY = config("SECRET_KEY")

DATABASES= {
        'default': dj_database_url.parse(config('DATABASE_URL'))
    }


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')