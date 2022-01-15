# -*- coding: utf-8 -*-
"""
Django settings for hamsterserv project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&h$*@kcen19u1o$v*_4fstsrpnosmv_rw1$&xi8&818rl&m55f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['si.graccs.gob.ni', 'localhost', '127.0.0.1', '[::1]']

# X_FRAME_OPTIONS -> default 'DENY'
X_FRAME_OPTIONS = 'SAMEORIGIN'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin.apps.SimpleAdminConfig',  # 'django.contrib.admin', -- Reemplazado para implementar admin personalizado
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_filters',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'django_bootstrap5',
    'django_bootstrap_icons',
    'corsheaders',  
    'hamster',
    'suir',
    'sispro',
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
    'django_social_share'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://si.graccs.gob.ni',
    'http://si.graccs.gob.ni:8000',
    'http://localhost',
    'http://localhost:8000',
    'http://127.0.0.1',
    'http://127.0.0.1:8000',
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'hamsterserv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',   #Agregado para usar archivos cargados por usuarios en los templates
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hamsterserv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'hamster',
#        'USER': 'hamster_user',
#        'PASSWORD': 'ze_h*Kd;3k64:}a(',
#        'HOST': '127.0.0.1',
#        'PORT': '3306',
#    }
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'portal_graccs',
        'USER': 'portaluser',
        'PASSWORD': 'p7xh&LkH)/Bv@$z6',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Managua'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media upload storage

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # '/var/www/graccs.gob.ni/media/'
MEDIA_URL = '/media/'

# Django rest_framework configurations

REST_FRAMEWORK = {
    
    # Usamos los permisos estándar de Django de django.contrib.auth,
    # o damos acceso de solo lectura a usuarios no autenticados.

    #'DEFAULT_PERMISSION_CLASSES' : [
    #    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #]
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# Django WYSIWYG settings for rich text editor with CKEditor

# DJANGO_WYSIWYG_FLAVOR = 'ckeditor'

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

CKEDITOR_UPLOAD_PATH = 'ckeditor/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_THUMBNAIL_SIZE = (75, 75)

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic'],
        ],
        'toolbar_SuirToolbar': [
            {'name': 'document', 'items': ['Source', '-', 'Preview']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            '/',
            {'name': 'basicStyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
            'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image','Image2', 'Embed', 'Youtube', 'Table', 'HorizontalRule', 'SpecialChar']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'toolbar': 'SuirToolbar',
        'tabSpaces': 4,
        'height': 291,
        'width': '100%',
        'removePlugins': 'stylesheetparser', #['stylesheetparser', 'image'],
        'allowedContent': True,
        'extraAllowedContent': 'iframe[*]',
        'extraPlugins': ','.join([
            'autolink',
            'autoembed',
            'clipboard',
            'dialog',
            'dialogui',
            'embedsemantic',
            'image2',
            'iframe',
            'iframedialog',
            'language',
            'uploadimage',
            'widget',
            'youtube',
            ]),
    }
}

SUIR_CONF = {
    'paginas': 12,
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SISPRO_CONF = {
    'paginas':20,
    'tipos-error':[
        'error de validación',
        'accceso denegado',
        'permisos de usuario',
        'propiedad de registro',
    ],
    'mensajes-error':{
        'validacion':"la sesión ha expirado. por favor, ingrese nuevamente con su nombre de usuario y contraseña.",
        'acceso':"Usted no tiene acceso para ejecutar la operación solicitada.",
        'permisos':"Su usuario no cuenta con los permisos para realizar la operación solicitada. Consulte con el administrador del sistema.",
        'propietario':"Usted no es el propietario/digitador del registro. Por este motivo, no tiene permiso de modificación. Consulte con el administrador del sistema.",
    }
}

HITCOUNT_KEEP_HIT_ACTIVE = {'hours':12}

HITCOUNT_HITS_PER_IP_LIMIT = 0




