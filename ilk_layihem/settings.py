
from pathlib import Path
import os
from telnetlib import AUTHENTICATION
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h)pj0^+s9b(l&n_om2o#fgejeje4u2=aoe)r#&4&92!@1#g0*s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL='accounts.User'
# Application definition

INSTALLED_APPS = [
    'modeltranslation',    # dil ucun
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'blog',
    'contact',
    'product',
    'accounts',
   # 'social.apps.django_app.default'
    'social_django',  #facebookla login olmaq ucun applerden sonra yazilmalidir

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # dil ucundur sessiondan sonra yerlesmelidir
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'ilk_layihem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',   # dil ucun
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'ilk_layihem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend',
                         'social_core.backends.facebook.FacebookOAuth2',
                         'social_core.backends.google.GoogleOAuth2',
                      ]    #facebookla login olmaq ucun

from django.urls import reverse_lazy
LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('home:index')
LOGOUT_URL = reverse_lazy('accounts:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('accounts:login')                        

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_FACEBOOK_KEY='679178576573305'
SOCIAL_AUTH_FACEBOOK_SECRET='f8b018ec97afe76e1d1e5ff9d4aaf862'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '588170983118-t2qh4j62cmrq1u4tejfltr29kcptjjve.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('az', ugettext('Azerbaijan')),
    ('ru', ugettext('Russian')),

)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
#-----------------------------------diller ucun bura qeder
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#--------------------- registrasiyanin dogrulanmasi ucun emaile link atmag ucun
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'z.jamal.saida@gmail.com'
EMAIL_HOST_PASSWORD = 'mjtjahuokvepuqrz'
#---------------------------------------------------------------------------------