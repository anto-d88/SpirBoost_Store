import os
from pathlib import Path
import environ

# ====================================================
# INITIALISATION
# ====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DJANGO_DEBUG=(bool, True),
    DJANGO_ENV=(str, "dev"),
)

env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(env_file)

# ====================================================
# CONFIGURATION DJANGO
# ====================================================

SECRET_KEY = env("DJANGO_SECRET_KEY", default="dev-secret-key-change-me")
DEBUG = env("DJANGO_DEBUG")
DJANGO_ENV = env("DJANGO_ENV")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

# ====================================================
# APPLICATIONS
# ====================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # App e-commerce
    "store",
]

# ====================================================
# MIDDLEWARE
# ====================================================

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
ASGI_APPLICATION = "spirboost_store.asgi.application"

# ====================================================
# BASE DE DONNÉES (LOCAL + RAILWAY)
# ====================================================

DATABASE_URL = env("DATABASE_URL", default="")

if DATABASE_URL:
    import dj_database_url
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=False
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ====================================================
# AUTHENTIFICATION
# ====================================================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ====================================================
# INTERNATIONALISATION
# ====================================================

LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = True

# ====================================================
# FICHIERS STATIQUES (LOCAL + PROD)
# ====================================================

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ====================================================
# SECURITÉ EN PROD
# ====================================================

if DJANGO_ENV == "prod":
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ====================================================
# SUPABASE (API)
# ====================================================

SUPABASE_URL = env("SUPABASE_URL", default="")
SUPABASE_ANON_KEY = env("SUPABASE_ANON_KEY", default="")
SUPABASE_SERVICE_ROLE_KEY = env("SUPABASE_SERVICE_ROLE_KEY", default="")

# ====================================================
# VALEUR PAR DÉFAUT
# ====================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
