"""
Django settings for Anarchy & Lace.

Goals:
- Local dev: optional .env + SQLite + console email
- Heroku staging: env vars + DATABASE_URL (Postgres) + WhiteNoise static
- Minimal + reversible config changes
"""

from pathlib import Path
import os

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------
def env_bool(name: str, default: bool = False) -> bool:
    return os.environ.get(name, str(default)).lower() in ("1", "true", "yes", "on")


# Optional: load .env locally (safe on Heroku)
try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    pass


# ---------------------------------------------------------
# Core settings
# ---------------------------------------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-dev-only-change-me")
DEBUG = env_bool("DJANGO_DEBUG", False)


# ---------------------------------------------------------
# Hosts / Security
# ---------------------------------------------------------
if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]
else:
    # Heroku apps live on *.herokuapp.com (and later your custom domain)
    ALLOWED_HOSTS = [".herokuapp.com"]

# Optional additional hosts, comma-separated:
# DJANGO_ALLOWED_HOSTS="anarchyandlace.co.uk,www.anarchyandlace.co.uk"
extra_hosts = [
    h.strip()
    for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
    if h.strip()
]
ALLOWED_HOSTS += extra_hosts

# CSRF trusted origins (recommended on Heroku/custom domains)
CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]

# Heroku proxy/HTTPS header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Keep staging flexible: only force HTTPS if you explicitly enable it
SECURE_SSL_REDIRECT = env_bool("DJANGO_SECURE_SSL_REDIRECT", False)


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
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files on Heroku
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
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # allauth needs this
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
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    # Heroku uses DATABASE_URL for Postgres
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
        )
    }

    # IMPORTANT:
    # Only require SSL for Postgres. Do NOT force sslmode on SQLite.
    if DATABASE_URL.startswith("postgres"):
        DATABASES["default"].setdefault("OPTIONS", {})
        DATABASES["default"]["OPTIONS"]["sslmode"] = "require"

else:
    # Local default: SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
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
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

# Media note:
# Heroku filesystem is ephemeral. MEDIA_* is fine locally,
# but you'll want Cloudinary/S3 (or static seed images) for staging.
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

# New-style allauth (avoid deprecated settings):
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

# Staging-friendly default: "mandatory" can be painful unless email is configured
ACCOUNT_EMAIL_VERIFICATION = os.environ.get("ACCOUNT_EMAIL_VERIFICATION", "optional")

ACCOUNT_FORMS = {
    "signup": "core.forms.CustomerSignupForm",
}

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
EMAIL_BACKEND = os.environ.get(
    "DJANGO_EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend",
)

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "no-reply@anarchyandlace.local")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env_bool("EMAIL_USE_TLS", True)


# ---------------------------------------------------------
# Stripe (placeholders)
# ---------------------------------------------------------
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
