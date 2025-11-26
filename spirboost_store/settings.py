import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------
# Ì¥ê SECRET KEY
# ------------------------------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key")

# ------------------------------------------------
# Ì¥ß DEBUG MODE
# ------------------------------------------------
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# ------------------------------------------------
# Ìºç ALLOWED HOSTS (Railway)
# ------------------------------------------------
ALLOWED_HOSTS = ["*"]

# ------------------------------------------------
# Ì≥¶ INSTALLED APPS
# ------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
]

# ------------------------------------------------
# Ì∑± MIDDLEWARE
# ------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "spirboost_store.urls"

# ------------------------------------------------
# Ìæ® TEMPLATES
# ------------------------------------------------
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
            ],
        },
    },
]

WSGI_APPLICATION = "spirboost_store.wsgi.application"

# ------------------------------------------------
# Ì¥ê PASSWORD VALIDATORS
# ------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ------------------------------------------------
# Ìºê LANGUAGE / TIME
# ------------------------------------------------
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = True

# ------------------------------------------------
# Ì≥Å STATIC FILES (Railway + WhiteNoise)
# ------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ------------------------------------------------
# Ì≥Å MEDIA FILES
# ------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------------------------
# Ìª° CSRF (Railway)
# ------------------------------------------------
CSRF_TRUSTED_ORIGINS = [
    "https://*.up.railway.app",
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ------------------------------------------------
# Ì∑Ñ DATABASE (LOCAL + PROD)
# ------------------------------------------------
ENV = os.environ.get("DJANGO_ENV", "development")

if ENV == "production":
    DATABASES = {
        "default": dj_database_url.parse(
            os.environ.get("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
