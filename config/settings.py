import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEFAULT=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "mptt",
    "ckeditor",
    "modeltranslation",
    "django_minio_backend.apps.DjangoMinioBackendConfig",
    "core.apps.CoreConfig",
    "product.apps.ProductConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {"default": env.db()}
DATABASES["default"]["DISABLE_SERVER_SIDE_CURSORS"] = True

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation." "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_STORAGE = "django_minio_backend.models.MinioBackend"

MINIO_ENDPOINT = env.str("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = env.str("MINIO_ACCESS_KEY")
MINIO_REGION = env.str("MINIO_REGION")
MINIO_SECRET_KEY = env.str("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = env.str("MINIO_BUCKET_NAME")
MINIO_SECURE = env.bool("MINIO_SECURE", False)
MINIO_USE_HTTPS = MINIO_SECURE

MINIO_CONSISTENCY_CHECK_ON_START = env.bool(
    "MINIO_CONSISTENCY_CHECK_ON_START", False
)

MINIO_PUBLIC_BUCKETS = [MINIO_BUCKET_NAME]
MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
MODELTRANSLATION_LANGUAGES = ("uz", "ru", "en")

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": [
            [
                "Bold",  # Жирность
                "Italic",  # Курсив
                "Underline",  # Подчеркивание
                "Strike",  # Перечеркнутый текст
                "TextColor",  # Цвет текста
                "FontSize",  # Размер шрифта
                "-",
                "NumberedList",  # Нумерованный список
                "BulletedList",  # Маркированный список
                "-",
                "Table",  # Таблицы
                "Link",  # Ссылки
            ],
            ["Undo", "Redo"],  # Отмена и повтор
        ],
        "stylesSet": [
            {
                "name": "Numbered List",
                "element": "ol",
                "styles": {"list-style-type": "decimal"},  # Нумерация
            },
            {
                "name": "Bulleted List (Dots)",
                "element": "ul",
                "styles": {"list-style-type": "disc"},  # Точки для списка
            },
            {
                "name": "Bold Text",
                "element": "span",
                "attributes": {"style": "font-weight: bold;"},
            },
            {
                "name": "Italic Text",
                "element": "span",
                "attributes": {"style": "font-style: italic;"},
            },
            {
                "name": "Underlined Text",
                "element": "span",
                "attributes": {"style": "text-decoration: underline;"},
            },
            {
                "name": "Strikethrough Text",
                "element": "span",
                "attributes": {"style": "text-decoration: line-through;"},
            },
            {
                "name": "Text Size (Large)",
                "element": "span",
                "attributes": {"style": "font-size: 18px;"},
            },
            {
                "name": "Text Size (Small)",
                "element": "span",
                "attributes": {"style": "font-size: 12px;"},
            },
        ],
        "height": 300,
        "width": 700,
    },
}
