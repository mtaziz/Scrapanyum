# app specific urls
from django.conf.urls import url
from Proxifier.views import proxifier, proxifier_ajax

urlpatterns = [
    url(r'^proxifier_ajax', proxifier_ajax),
    url(r'^proxifier', proxifier),
]
