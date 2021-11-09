"""
Django settings for nhsx project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

# stdlib
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from datetime import date, timedelta

# Try to import envkey, otherwise trust that the environment variables
# are being injected another way
try:
    import envkey  # NOQA
except Exception:
    pass


####################################################################################################
# File system and misc
####################################################################################################

PROJECT_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(PROJECT_DIR)
ENABLE_PROFILER = False
THE_FUTURE = date.today() + timedelta(days=365 * 10)

WAGTAILEMBEDS_RESPONSIVE_HTML = True
PAGINATION_ITEMS_PER_PAGE = 10

# Suppress error messages from upgrading to Django 3.2 by keeping the old 32-bit ID number field
# https://koenwoortman.com/python-django-auto-created-primary-key-used-when-not-defining-primary-key-type/
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

####################################################################################################
# Django Dev Panel recommendations and other security
####################################################################################################


SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
CSRF_USE_SESSIONS = False

WAGTAIL_2FA_REQUIRED = False


####################################################################################################
# Installed Apps
####################################################################################################

DJANGO_APPS = [
    "whitenoise.runserver_nostatic",
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.forms",
    "django_extensions",
    "modelcluster",
    "taggit",
    "storages",
    "django_assets",
    "cacheops",
    "django_otp",
    "django_otp.plugins.otp_totp",
]

WAGTAIL_APPS = [
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "wagtail.contrib.forms",
    "wagtail.contrib.settings",
    "wagtail.contrib.table_block",
    "wagtail.contrib.modeladmin",
    "wagtailfontawesome",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.routable_page",
    "wagtailnhsukfrontend",
    "wagtailcache",
    "wagtail_2fa",
]

SITE_APPS = [
    "modules.home",
    "modules.search",
    "modules.core",
    "modules.images",
    "modules.documents",
    "modules.users",
    "modules.blog_posts",
    "modules.publications",
    "modules.news",
    "modules.ai_lab",
    "modules.people",
    "modules.meeting_minutes",
    "modules.ig_guidance",
    "modules.case_studies",
]

INSTALLED_APPS = WAGTAIL_APPS + DJANGO_APPS + SITE_APPS


####################################################################################################
# Middleware
####################################################################################################


MIDDLEWARE = [
    # FIRST
    "wagtailcache.cache.UpdateCacheMiddleware",  # MUST BE FIRST
    "django.middleware.security.SecurityMiddleware",  # SHOULD BE SECOND
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    # SESSION
    "django.contrib.sessions.middleware.SessionMiddleware",
    # COMMON
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    # SECURITY
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "wagtail_2fa.middleware.VerifyUserMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # ROLLBAR
    "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
    # CACHE
    "wagtailcache.cache.FetchFromCacheMiddleware",  # MUST BE LAST
]


####################################################################################################
# Core Django config
####################################################################################################


ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", None)
INTERNAL_IPS = ["127.0.0.1"]
APPEND_SLASH = True


####################################################################################################
# Database
####################################################################################################


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB", ""),
        "USER": os.environ.get("POSTGRES_USER", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        "TEST": {"NAME": "test_{}".format(os.environ.get("POSTGRES_DB", None))},
    }
}


####################################################################################################
# Search
####################################################################################################


WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.contrib.postgres_search.backend",
        "SEARCH_CONFIG": "english",
        "AUTO_UPDATE": True,
    }
}


####################################################################################################
# Template
####################################################################################################


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"


####################################################################################################
# Rollbar
####################################################################################################


ROLLBAR = {
    "access_token": os.environ.get("POST_SERVER_ITEM_ACCESS_TOKEN", ""),
    "environment": os.environ.get("SERVER_ENV", "development"),
    "branch": "master",
    "root": "/usr/srv/app",
}


####################################################################################################
# Password validators
####################################################################################################


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 10},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

####################################################################################################
# Translations and Locales
####################################################################################################

# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_L10N = True
USE_TZ = True


####################################################################################################
# Project specific settings
####################################################################################################


AUTH_USER_MODEL = "users.User"
WAGTAILIMAGES_IMAGE_MODEL = "images.NHSXImage"
WAGTAILDOCS_DOCUMENT_MODEL = "documents.NHSXDocument"
WAGTAIL_SITE_NAME = "NHSX"
WAGTAILEMBEDS_FINDERS = [
    {
        "class": "helpers.finders.OSMFinder",
        # Any other options will be passed as kwargs to the __init__ method
    }
]

DEFAULT_AUTHOR_AVATAR = "avatar.png"

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    "default": {
        "WIDGET": "wagtail.admin.rich_text.DraftailRichTextArea",
        "OPTIONS": {
            "features": [
                "h2",
                "h3",
                "h4",
                "ol",
                "ul",
                "hr",
                "bold",
                "italic",
                "link",
                "document-link",
                "image",
            ]
        },
    },
    "alt": {"WIDGET": "wagtail.admin.rich_text.HalloRichTextArea"},
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
TAG_SPACES_ALLOWED = True


####################################################################################################
# Session and Cache
####################################################################################################


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session_cache"
WAGTAIL_CACHE_BACKEND = "wagtail_cache"
WAGTAIL_CACHE = True

REDIS_HOST = os.environ.get("REDIS_HOST", "")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_HOST_FULL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
REDIS_HOST_CACHEOPS = f"{REDIS_HOST_FULL}/1"
REDIS_HOST_PAGECACHE = f"{REDIS_HOST_FULL}/2"
REDIS_HOST_SESSIONS = f"{REDIS_HOST_FULL}/3"


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_HOST_CACHEOPS,
        "OPTIONS": {
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ.get("REDIS_PASSWORD"),
            "IGNORE_EXCEPTIONS": True,
        },
    },
    "wagtail_cache": {
        "BACKEND": "wagtailcache.compat_backends.django_redis.RedisCache",
        "LOCATION": REDIS_HOST_PAGECACHE,
        "TIMEOUT": 60 * 15,  # Fifteen minutes
        "OPTIONS": {
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ.get("REDIS_PASSWORD"),
            "IGNORE_EXCEPTIONS": True,
        },
    },
    "session_cache": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_HOST_SESSIONS,
        "OPTIONS": {
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.environ.get("REDIS_PASSWORD"),
            "IGNORE_EXCEPTIONS": True,
        },
    },
}


####################################################################################################
# CacheOps Config
####################################################################################################

CACHEOPS_ENABLED = True
CACHEOPS_LRU = True

CACHEOPS_REDIS = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "db": 1,
    "socket_timeout": 3,
    "password": os.environ.get("REDIS_PASSWORD", None),
}

CACHEOPS = {
    # Light caching - 15 mins
    "wagtailcore.pageviewrestriction": {"ops": "all", "timeout": 60 * 60},
    # Regular caching - 1 hour
    "auth.permission": {"ops": "all", "timeout": 60 * 60},
    "auth.user": {"ops": "all", "timeout": 60 * 60},
    "wagtaildocs.document": {"ops": "all", "timeout": 60 * 60},
    "wagtailcore.collection": {"ops": "all", "timeout": 60 * 60},
    "wagtailimages.image": {"ops": "all", "timeout": 60 * 60},
    "wagtailimages.Rendition": {"ops": "all", "timeout": 60 * 60},
    "images.nhsximage": {"ops": "all", "timeout": 60 * 60},
    "images.nhsxrendition": {"ops": "all", "timeout": 60 * 60},
    # Aggressive caching - 24 hours
    "wagtailcore.site": {"ops": "all", "timeout": 60 * 60 * 24},
    "django.content_type": {"ops": "all", "timeout": 60 * 60 * 24},
    # Enable manual caching on all other models with default timeout of an hour
    # Use Post.objects.cache().get(...)
    #  or Tags.objects.filter(...).order_by(...).cache()
    # to cache particular ORM request.
    # Invalidation is still automatic
    # "*.*": {"ops": (), "timeout": 60 * 60},g
    # Disable caching on migrations
    "migrations.*": {"ops": (), "timeout": 0},
}


####################################################################################################
# Shell Plus
####################################################################################################


SHELL_PLUS = "ipython"
# SHELL_PLUS_POST_IMPORTS = (
#     ("modules.home.service", "*"),
# )


####################################################################################################
# SECURITY
####################################################################################################


# This will allow the cache to swallow the fact that the website is behind TLS
# and inform the Django using "X-Forwarded-Proto" HTTP header.
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# This is a setting setting HSTS header. This will enforce the visitors to use
# HTTPS for an amount of time specified in the header. Please make sure you
# consult with sysadmin before setting this.
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-hsts-seconds
if "SECURE_HSTS_SECONDS" in os.environ:
    SECURE_HSTS_SECONDS = int(os.environ["SECURE_HSTS_SECONDS"])


# Required if wish to submit to browser HSTS preload list at https://hstspreload.org/
# Will be ignored if `SECURE_HSTS_SECONDS` is not set
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECURE_HSTS_INCLUDE_SUBDOMAINS
if os.environ.get("SECURE_HSTS_INCLUDE_SUBDOMAINS", "false").lower().strip() == "true":
    SECURE_HSTS_INCLUDE_SUBDOMAINS = (
        True  # IMPT: this will enforce HTTPS for all subdomains!
    )


# Required if wish to submit to browser HSTS preload list at https://hstspreload.org/
# Will be ignored if `SECURE_HSTS_SECONDS` is not set
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECURE_HSTS_PRELOAD
if os.environ.get("SECURE_HSTS_PRELOAD", "false").lower().strip() == "true":
    SECURE_HSTS_PRELOAD = True


# Required if wish to submit to browser HSTS preload list at https://hstspreload.org/
if os.environ.get("PREPEND_WWW", "false").lower().strip() == "true":
    PREPEND_WWW = True


# https://docs.djangoproject.com/en/stable/ref/settings/#secure-browser-xss-filter
if os.environ.get("SECURE_BROWSER_XSS_FILTER", "true").lower().strip() == "true":
    SECURE_BROWSER_XSS_FILTER = True


# https://docs.djangoproject.com/en/stable/ref/settings/#secure-content-type-nosniff
if os.environ.get("SECURE_CONTENT_TYPE_NOSNIFF", "true").lower().strip() == "true":
    SECURE_CONTENT_TYPE_NOSNIFF = True


# Referrer-policy header settings.
# https://django-referrer-policy.readthedocs.io/en/1.0/

REFERRER_POLICY = os.environ.get(
    "SECURE_REFERRER_POLICY", "no-referrer-when-downgrade"
).strip()


####################################################################################################
# Static assets
####################################################################################################

ASSETS_ROOT = "{}/assets".format(BASE_DIR)
ASSETS_DEBUG = False
ASSETS_AUTO_BUILD = False
ASSETS_MODULES = ["config.assets"]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_FINDERS = [
    "django_assets.finders.AssetsFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets", "dist"),
]


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "nhsx"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "http://nhsx.test"


####################################################################################################
# Postmark
####################################################################################################

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.environ.get(
    "DEFAULT_FROM_EMAIL", "nhsx-website@clients.dxw.com"
)
DEFAULT_FROM_EMAIL = os.environ.get(
    "DEFAULT_FROM_EMAIL", "nhsx-website@clients.dxw.com"
)
SERVER_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "nhsx-website@clients.dxw.com")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = str(os.environ.get("EMAIL_HOST_URL", ""))
EMAIL_HOST_USER = str(os.environ.get("EMAIL_HOST_USER", ""))
EMAIL_HOST_PASSWORD = str(os.environ.get("EMAIL_HOST_PASSWORD", ""))
EMAIL_PORT = str(os.environ.get("EMAIL_HOST_PORT", "587"))
EMAIL_USE_TLS = True
