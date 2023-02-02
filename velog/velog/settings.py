"""
Django settings for velog project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import json
import os
import sys

from environ import Env
from datetime import timedelta
from pathlib import Path

import pymysql  
pymysql.install_as_MySQLdb()

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env_path = BASE_DIR / ".env"
if env_path.exists():
    with env_path.open("rt", encoding="utf8") as f:
        env.read_env(f, overwrite=True)

# STATE =os.environ.get("STATE")
STATE=env("STATE")
# SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = env("SECRET_KEY")
# SOCIAL_AUTH_GOOGLE_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_SECRET")
SOCIAL_AUTH_GOOGLE_SECRET = env("SOCIAL_AUTH_GOOGLE_SECRET")
# SOCIAL_AUTH_GOOGLE_CLIENT_ID = os.environ.get("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_CLIENT_ID = env("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
FACEBOOK_CLIENT_ID = env("FACEBOOK_CLIENT_ID")
FACEBOOK_SECRET_KEY = env("FACEBOOK_SECRET_KEY")
GH_CLIENT_ID = env("GH_CLIENT_ID")
GH_SECRET_KEY = env("GH_SECRET_KEY")
KAKAO_CLIENT_ID = env("KAKAO_CLIENT_ID")
KAKAO_SECRET_KEY = env("KAKAO_SECRET_KEY")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# secret_file = os.path.join(BASE_DIR, "secrets.json")

# with open(secret_file) as f:
#     secrets = json.loads(f.read())

# for key, value in secrets.items():
#    setattr(sys.modules[__name__], key, value)


def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# SECRET_KEY = get_secret("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*", "https://api.7elog.store", "43.201.111.105", "https://7elog.store"]


# Application definition

INSTALLED_APPS = [
    # cors
    "corsheaders",
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # app
    "authentication.apps.AuthenticationConfig",
    "velogapp.apps.VelogappConfig",
    # drf
    "drf_yasg",
    # 'djoser',
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt.token_blacklist",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # allauth
    "allauth_ui",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.kakao",
    "widget_tweaks",
]

REST_USE_JWT = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"

SITE_ID = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"

AUTH_USER_MODEL = "authentication.User"

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "authentication.serializers.UserSerializer",
    "LOGIN_SERIALIZER": "authentication.serializers.UserLoginSerializer",
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "authentication.serializers.CustomRegisterSerializer"
}

REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "errors",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
    "PAGE_SIZE": 10,
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "velog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "velog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'team7elogdb',
        'USER': 'admin',
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '3306',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = '/home/ubuntu/velog/static/'
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Social Login

# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         "SCOPE": [
#             "profile",
#             "email",
#         ],
#         "AUTH_PARAMS": {
#             "access_type": "online",
#         },
#         "OAUTH_PKCE_ENABLED": True,
#     },
#     "facebook": {
#         "METHOD": "oauth2",
#         "AUTH_PARAMS": {"auth_type": "reauthenticate"},
#         "INIT_PARAMS": {"cookie": True},
#         "FIELDS": [
#             "id",
#             "email",
#             "name",
#             "name_format",
#             "picture",
#             "short_name",
#         ],
#         "EXCHANGE_TOKEN": True,
#         # 'LOCALE_FUNC': 'path.to.callable',
#         "VERIFIED_EMAIL": False,
#         "VERSION": "v13.0",
#         "GRAPH_API_URL": "https://graph.facebook.com/v13.0",
#     },
# }

LOGIN_REDIRECT_URL = "/api/v1/"
LOGOUT_REDIRECT_URL = "/api/v1/accounts/login/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/api/v1/accounts/login/"
# LOGOUT_REDIRECT_URL = "/api/v1/accounts/logout/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True  # TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
URL_FRONT = 'https://7elog.store'
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
EMAIL_CONFIRMATION_EXPIRE_DAYS: 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[이메일 인증] "
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/api/v1/"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/api/v1/accounts/login/"
# EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/api/v1/"

LOGIN_REDIRECT_URL = "/auth/social/login"
LOGOUT_REDIRECT_URL = "/auth/social/logout"

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://d822df5kj1qhh.cloudfront.net",
    "https://api.7elog.store",
    "https://7elog.store",
    "http://localhost:3000",
    "http://localhost:80",
    "http://127.0.0.1:9000",
    'https://*.7elog.store',
    'http://7elog.store',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.7elog\.store$",
]
CORS_ORIGIN_WHITELIST = [
    'https://d822df5kj1qhh.cloudfront.net',
    'http://7elog.store',
    'https://*.7elog.store',
    'localhost:3000',
    'localhost:8000',
    '127.0.0.1:8000',
    'https://7elog.store',
    'https://api.7elog.store',
]
# SECURE_CROSS_ORIGIN_OPENER_POLICY = None

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = (
    'access-control-allow-credentials',
    'access-control-allow-origin',
    'access-control-request-method',
    'access-control-request-headers',
    'accept',
    'accept-encoding',
    'accept-language',
    'authorization',
    'connection',
    'content-type',
    'dnt',
    'credentials',
    'host',
    'origin',
    'user-agent',
    'X-CSRFToken',
    'csrftoken',
    'x-requested-with',
)

# CSRF
CSRF_TRUSTED_ORIGINS = [ 
    'https://7elog.store',
    'http://api.7elog.store',
    'https://api.7elog.store',
    'https://*.7elog.store',
    'http://7elog.store',
    'https://d822df5kj1qhh.cloudfront.net',
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'encoding': 'utf-8',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'mysite.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'my': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}
