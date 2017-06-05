# app specific urls
from django.conf.urls import url
from Scraper.views import *

urlpatterns = [
    url(r'^manager', trip_manager_view),
    url(r'^task_schedule', task_scheduler_view),
]
