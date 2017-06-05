from __future__ import unicode_literals
from Core.models import Client, Business, Batch
from django.contrib import admin

admin.site.register(Client)
admin.site.register(Business)
admin.site.register(Batch)