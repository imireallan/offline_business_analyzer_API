"""
Django settings for offline_business_analyzer project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get('SECRET_KEY'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	# My apps
	'offline_business_analyzer.apps.account.apps.AccountConfig',
	'offline_business_analyzer.apps.business.apps.BusinessConfig',
	'offline_business_analyzer.apps.transaction.apps.TransactionConfig',

	# django apps
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# installed apps
	'rest_framework',
	'rest_framework.authtoken',
	'csvimport.app.CSVImportConf',
	'storages',
	'corsheaders'
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'offline_business_analyzer.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
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

# custom user model
AUTH_USER_MODEL = 'account.User'

WSGI_APPLICATION = 'offline_business_analyzer.wsgi.application'

# REST_FRAMEWORK settings
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.TokenAuthentication'
	],
	'DEFAULT_RENDERER_CLASSES': [
		'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
		'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
		# Any other renders
	],

	'DEFAULT_PARSER_CLASSES': [
		# If you use MultiPartFormParser or FormParser, we also have a camel case version
		'djangorestframework_camel_case.parser.CamelCaseFormParser',
		'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
		'djangorestframework_camel_case.parser.CamelCaseJSONParser',
		# Any other parsers
	],
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.environ.get('DB_NAME'),
		'USER': os.environ.get('DB_USER'),
		'PASSWORD': os.environ.get('DB_PASSWORD'),
		'HOST': os.environ.get('DB_HOST'),
		'PORT': os.environ.get('DB_PORT')

	}
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# AWS_UPLOAD_BUCKET =

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# AWS_UPLOAD_USERNAME =

# AWS_UPLOAD_GROUP =

# AWS_UPLOAD_REGION =

AWS_UPLOAD_ACCESS_KEY_ID = os.environ.get('AWS_UPLOAD_ACCESS_KEY_ID')

AWS_UPLOAD_SECRET_KEY = os.environ.get('AWS_UPLOAD_SECRET_KEY')

AWS_S3_FILE_OVERWRITE = os.environ.get('AWS_S3_FILE_OVERWRITE')

AWS_DEFAULT_ACL = os.environ.get('AWS_DEFAULT_ACL')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CORS_ORIGIN_ALLOW_ALL = True

django_heroku.settings(locals())
