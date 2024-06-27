from .base import *
import dj_database_url

SECRET_KEY = config("SECRET_KEY")

# DATABASES= {
#         'default': dj_database_url.parse(config('DATABASE_URL'))
#     }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'cardealership/static')]
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)