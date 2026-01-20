"""
Django settings for Anarchy & Lace.

- Local dev uses .env (optional) + SQLite + console email
- Production (e.g. Heroku) uses environment variables + DATABASE_URL + WhiteNoise
"""

from __future__ import annotations

import os
from pathlib import Path

import dj_database_url

# Optional: load .env locally (safe to ignore if not present / not installed)
try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    pass


# ---------------------------------------------------------
# Base
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.environ.get("DJANGO_ENV", "development").lower()

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-only-change-me",
)

# NOTE: default False so you don't accidentally ship DEBUG=True
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# Heroku sets DYNO in the environment
ON_HEROKU = "DYNO" in os.environ


# ---------------------------------------------------------
# Hosts / Security
# ---------------------------------------------------------

if DEBUG and not ON_HEROKU:
    # Local dev
    ALLOWED_HOSTS = [
        "127.0.0.1",
        "localhost",
        "testserver",
    ]
else:
    # Production / Heroku (or when running DEBUG on Heroku for diagnostics)
    env_hosts = os.environ.get("DJANGO_ALLOWED_HOSTS", "")
    ALLOWED_HOSTS = [h.strip() for h in env_hosts.split(",") if h.strip()]

    # Always allow Heroku app subdomains when on Heroku
    if ON_HEROKU and ".herokuapp.com" not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(".herokuapp.com")

    # Safety fallback so we never end up with an empty list
    if not ALLOWED_HOSTS:
        ALLOWED_HOSTS = [".herokuapp.com"]

# Needed for HTTPS domains (set as comma-separated list)
CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]

# Recommended when behind a proxy (Heroku)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# ---------------------------------------------------------
# Applications
# ---------------------------------------------------------

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.apple",
    # Local apps
    "home",
    "core",
    "catalog",
    "manager",
    "cart",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ---------------------------------------------------------
# URLs / Templates / WSGI
# ---------------------------------------------------------

ROOT_URLCONF = "anarchy_and_lace.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # shared templates folder
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


# ---------------------------------------------------------
# Database
# ---------------------------------------------------------
# Heroku provides DATABASE_URL automatically when Postgres is attached.
# Locally we fall back to SQLite if DATABASE_URL is not set.

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False,
    )
}


# ---------------------------------------------------------
# Password validation
# ---------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ---------------------------------------------------------
# Internationalization
# ---------------------------------------------------------

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------
# Static & Media
# ---------------------------------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # your local static folder
STATIC_ROOT = BASE_DIR / "staticfiles"  # collectstatic target on Heroku/production

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ---------------------------------------------------------
# Defaults
# ---------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ---------------------------------------------------------
# Sites / Auth / Allauth
# ---------------------------------------------------------

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

# --- Updated Allauth settings (avoids the deprecation warnings you saw) ---
# Email-only login:
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

# Verification:
# - local dev is fine as "mandatory" because emails print to console
# - for easier testing without clicking links, set env ACCOUNT_EMAIL_VERIFICATION=optional (or none)
ACCOUNT_EMAIL_VERIFICATION = os.environ.get("ACCOUNT_EMAIL_VERIFICATION", "mandatory")

# Use your custom signup form (profile fields)
ACCOUNT_FORMS = {
    "signup": "core.forms.CustomerSignupForm",
}

# Social provider config (optional; real keys can also be set via SocialApp in admin)
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


# ---------------------------------------------------------
# Email
# ---------------------------------------------------------
# Local dev: print emails to console so Allauth doesn't crash when verifying.
# Production later: swap to SMTP via env vars.

EMAIL_BACKEND = os.environ.get(
    "DJANGO_EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend",
)

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "no-reply@anarchyandlace.local")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# If you set DJANGO_EMAIL_BACKEND to SMTP in the future, these will be used:
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True") == "True"


# ---------------------------------------------------------
# Stripe (placeholders for later)
# ---------------------------------------------------------

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
