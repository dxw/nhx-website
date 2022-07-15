import os
from .remote import *  # NOQA
from .base import MEDIA_ROOT, BASE_DIR  # NOQA

DEBUG = False

BASE_URL = "https://transform.england.nhs.uk"

####################################################################################################
# Static assets served by Whitenoise
####################################################################################################


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


####################################################################################################
# Media assets served from a CDN / bucket
####################################################################################################


AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_CDN_URI", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME", "")
MEDIA_URL = "{}{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIA_ROOT)
