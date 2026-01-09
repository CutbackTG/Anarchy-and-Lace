import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-only-change-me",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# In production, set DJANGO_ALLOWED_HOSTS="example.com,www.example.com"
if DEBUG:
    # Include "testserver" so Django's test client (and some dev tools) work without DisallowedHost.
    ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]
else:
    ALLOWED_HOSTS = [
        h.strip()
        for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
        if h.strip()
    ]

# Application definition
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Allauth (accounts + optional social login)
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Social providers (only include what you use)
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.apple",
    # Local apps
    "home",
    "core",
    "catalog",
    "manager",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "anarchy_and_lace.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # shared templates folder at project root: /templates
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # required by allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "anarchy_and_lace.wsgi.application"

# Database (sqlite for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media (uploads, product images)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Sites framework (required by allauth)
SITE_ID = 1

# Authentication backends (required for allauth)
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Where to send users after login/logout
LOGIN_REDIRECT_URL = "/"                # after login
ACCOUNT_LOGOUT_REDIRECT_URL = "/"        # after logout

# Account behaviour
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"  # users sign in with email
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# IMPORTANT: Your tests expect signup to succeed without an "email2" field.
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False

# Use your custom signup form (Profile fields)
ACCOUNT_FORMS = {
    "signup": "core.forms.CustomerSignupForm",
}

# Optional social provider config (safe defaults; real keys go in SocialApp admin)
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("GOOGLE_CLIENT_ID", ""),
            "secret": os.environ.get("GOOGLE_CLIENT_SECRET", ""),
            "key": "",
        }
    },
    "facebook": {
        "APP": {
            "client_id": os.environ.get("FACEBOOK_CLIENT_ID", ""),
            "secret": os.environ.get("FACEBOOK_CLIENT_SECRET", ""),
            "key": "",
        }
    },
    "apple": {
        "APP": {
            "client_id": os.environ.get("APPLE_CLIENT_ID", ""),
            "secret": os.environ.get("APPLE_CLIENT_SECRET", ""),
            "key": "",
        }
    },
}
