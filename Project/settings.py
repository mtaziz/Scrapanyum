import djcelery
import os

djcelery.setup_loader()
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SECRET_KEY = '@ek-dyn_(h)=qi8f(jn*mr1^73x-gtiodm)^(bz7^v@n&$%rj4'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ALLOWED_HOSTS = ['34.249.182.70', 'ec2-34-249-182-70.eu-west-1.compute.amazonaws.com']


# Application definition
INSTALLED_APPS = [
    # pre-packaged
    'django.contrib.admin',
    # 'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Added libraries
    'dynamic_scraper',
    'djcelery',
    'coverage',
    'kombu.transport',
    'templateaddons',
    'django_crontab',
    'django_apscheduler',

    # Added by user
    'Core',
    'Scraper',
    'Proxifier',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'

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

WSGI_APPLICATION = 'Project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scrapanyum',
        'HOST': '/opt/bitnami/postgresql',

        'PORT': '5432',
        'USER': 'bitnami',
        'PASSWORD': '74b52e1548'
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BrandReportApp.settings")
BOT_NAME = 'Spider'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'Scraper.scraper', ]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.DjangoImagesPipeline',
    'dynamic_scraper.pipelines.ValidationPipeline',
    'open_news.scraper.pipelines.DjangoWriterPipeline',
]

IMAGES_STORE = os.path.join(PROJECT_ROOT, '../thumbnails')

IMAGES_THUMBS = {
    'small': (170, 170),
}

# django-celery settings
# djcelery.setup_loader()
#
# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_BACKEND = "django"
# BROKER_USER = "guest"
# BROKER_PASSWORD = "guest"
# BROKER_VHOST = "/"
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

