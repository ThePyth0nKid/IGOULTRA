from pathlib import Path

# === Project Base Directory ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Secret Key (keep this safe in production) ===
SECRET_KEY = 'django-insecure-suqsjqig8eix8o^r%b-9uqe772358g^)d*5s#%s$=z@t4g=0b_'

# === Debug mode (disable in production) ===
DEBUG = True

# === Allowed Hosts (Heroku + Local + Custom Domains) ===
ALLOWED_HOSTS = [
    'igoultra-c414ad8c1a00.herokuapp.com',
    'localhost',
    '127.0.0.1',
    'igo-ultra-landing.vercel.app',
    '.igoultra.de',
    '.igoultra.com'
]

# === Application Definition ===
INSTALLED_APPS = [
    # Core middleware dependencies
    'corsheaders',

    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.discord',

    # Local apps
    'xp_system',
    'users',

    # Required by allauth
    'django.contrib.sites',
]

# === Custom User Model (replaces default Django User) ===
AUTH_USER_MODEL = 'users.CustomUser'

# === Middleware Stack ===
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Handles CORS headers first
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files efficiently
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# === URL configuration ===
ROOT_URLCONF = 'ultrabutton.urls'

# === Template Settings ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add template directories here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === WSGI entry point for production ===
WSGI_APPLICATION = 'ultrabutton.wsgi.application'

# === Database (SQLite for development) ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Password Validators ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Internationalization ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Static Files ===
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Optimized for Heroku

# === Default Primary Key Field Type ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === Allauth Configuration ===
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/xp_system/profile/'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGIN_METHODS = {'username'}  # Optional override for login method
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

# === Django REST Framework Settings ===
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT-based auth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# === CORS Settings for Vite Frontend ===
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "https://igo-ultra-landing.vercel.app",
    # Alternative Vite dev port
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
