from django.conf.urls import url
from Core.views import *

urlpatterns = [
    url(r'^home', dashboard),
    url(r'^refresh_clients', refresh_client, name='get_clients'),
    url(r'^refresh_business', refresh_business, name='get_business')
    ,
    url(r'^create_client_ajax', create_client_ajax, name='create_client'),
    url(r'^create_business_ajax', create_business_ajax, name='create_business'),
    url(r'^create_batch_ajax', create_batch_ajax, name='create_batch'),

    url(r'^delete_client_ajax', delete_client_ajax, name='delete_client'),
    url(r'^delete_business_ajax', delete_business_ajax, name='delete_business'),
]
