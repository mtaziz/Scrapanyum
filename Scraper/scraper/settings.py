from __future__ import unicode_literals
# Scrapy settings for open_news project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

import os, sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../../../../"))
# only for example_project

BOT_NAME = 'happy_bot'

LOG_STDOUT = True

SPIDER_MODULES = ['dynamic_scraper.spiders', 'Scraper.scraper', ]
USER_AGENT = '{b}/{v}'.format(b=BOT_NAME, v='1.0')

ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'Scraper.scraper.pipelines.DjangoWriterPipeline': 800,
}

IMAGES_STORE = os.path.join(PROJECT_ROOT, '../thumbnails')

IMAGES_THUMBS = {
    'medium': (50, 50),
    'small': (25, 25),
}

DSCRAPER_IMAGES_STORE_FORMAT = 'ALL'

DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'INFO'
DSCRAPER_LOG_LIMIT = 5

# Splash for JavaScript support options

SPLASH_URL = 'http://192.168.1.54:8050'

DSCRAPER_SPLASH_ARGS = {
    'wait': 5.0,
    'max-timeout': 2600
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
