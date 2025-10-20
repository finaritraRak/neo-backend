"""
Django settings for neo_backend project.
"""

from pathlib import Path
import os
from datetime import timedelta
from decouple import config
from corsheaders.defaults import default_headers
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:5173')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '206.189.117.17', 
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'apps.core',
    'apps.users',
    "channels",
    'dashboard',
    'permissions',
    'settings',
    'ckeditor',  
    'ckeditor_uploader',  
    'django_ckeditor_5', 
    'notifications',
    'companies',
    'sites',
    'energy_data',
    'alarms',
]

ASGI_APPLICATION = 'neo_backend.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
       
    },
}

# Configuration Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "Lynkevo Admin",
    "site_header": "",
    "site_brand": "Lynkevo",
    "welcome_sign": "Bienvenue sur l'espace admin Lynkevo",
    "copyright": "Lynkevo. All rights reserved.",
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "site_logo": "admin/img/logo.png", 
    "site_logo_classes": "img-circle elevation-3",
    "site_icon": "admin/img/logo.png",
    "login_logo": None,
    "login_logo_dark": "admin/img/logo.png",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core": "fas fa-cog",
        "users": "fas fa-user-circle",
        "blog": "fas fa-blog",
        "seo": "fas fa-search",
        "services": "fas fa-concierge-bell",
        "testimonials": "fas fa-quote-left",
        "team": "fas fa-users",
    },
    "topmenu_links": [
        {"name": "Site public", "url": "/", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "mailto:support@lynkevo.com", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Site public", "url": "/", "icon": "fas fa-globe"},
    ],
    "show_ui_builder": DEBUG,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_color": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False,
    "custom_css": "css/custom.css",
    "custom_js": None,
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
  
]

ROOT_URLCONF = 'neo_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration pour l'ancien django-ckeditor (requis par l'application blog)
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': '100%',
        'extraPlugins': ','.join([
            'uploadimage', 'image2', 'autogrow'
        ]),
        'removePlugins': 'resize',
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'autoGrow_maxHeight': 600,
        'autoGrow_minHeight': 200,
    }
}

# Configuration CKEditor 5 (pour les tours)
CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "link", "underline", "strikethrough", "|",
            "bulletedList", "numberedList", "|",
            "blockQuote", "insertTable", "|",
            "imageUpload", "imageInsert", "|",
            "undo", "redo", "|",
            "alignment", "outdent", "indent"
        ],
        "language": "fr",
        "image": {
            "toolbar": [
                "imageTextAlternative", "toggleImageCaption", "imageStyle:alignLeft",
                "imageStyle:alignCenter", "imageStyle:alignRight"
            ],
            "styles": ["alignLeft", "alignCenter", "alignRight"]
        },
        "table": {
            "contentToolbar": ["tableColumn", "tableRow", "mergeTableCells", "tableProperties", "tableCellProperties"]
        },
        "height": 400,
        "removePlugins": ["Title"],
    },
    "extends": {
        "language": "fr",
        "removePlugins": ["Title"],
        "toolbar": [
            "heading", "|", "bold", "italic", "underline", "|",
            "link", "|", "bulletedList", "numberedList", "|",
            "blockQuote", "insertTable", "|", "imageUpload", "|", "undo", "redo"
        ],
    },
}

# Configuration du stockage et de l'upload pour CKEditor 5
CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
CKEDITOR_5_UPLOAD_PATH = "uploads/ckeditor/"

WSGI_APPLICATION = 'neo_backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom User Model
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

# Assure-toi que SessionAuthentication n'est PAS dans les classes d'authentification
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication', 
        # 'rest_framework.authentication.SessionAuthentication',  ← À COMMENTER ou SUPPRIMER
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # 🔥 Changer AllowAny → IsAuthenticated par défaut
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
   
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'x-site-id',
    'x-track-page',
]

CORS_ALLOW_CREDENTIALS = True

# Create required directories
os.makedirs(BASE_DIR / 'static', exist_ok=True)
os.makedirs(BASE_DIR / 'media', exist_ok=True)
os.makedirs(BASE_DIR / 'media' / 'uploads', exist_ok=True)
os.makedirs(BASE_DIR / 'media' / 'uploads' / 'ckeditor', exist_ok=True)
os.makedirs(BASE_DIR / 'templates', exist_ok=True)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)

if config('EMAIL_USE_SSL', default=False, cast=bool):
    EMAIL_USE_SSL = True
    EMAIL_USE_TLS = False
else:
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)

PROJECT_LANGUAGES = ['fr', 'en']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.seo': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


DATA_UPLOAD_MAX_MEMORY_SIZE = 2684354560 

FILE_UPLOAD_MAX_MEMORY_SIZE = 2684354560