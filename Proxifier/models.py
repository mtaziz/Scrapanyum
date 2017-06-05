from __future__ import unicode_literals
from django.db import models


class ProxifierAccount(models.Model):
    class Meta:
        app_label = 'Proxifier'

    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    alt_mail = models.CharField(max_length=30, blank=True, null=True)
    browser = models.CharField(max_length=30, blank=True, null=True)

    user_agent = models.TextField(blank=True, null=True)
    plugin_list = models.CharField(max_length=300, blank=True, null=True)
    screen_width = models.CharField(max_length=300, blank=True, null=True)
    screen_height = models.CharField(max_length=300, blank=True, null=True)
    profile_file = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.user_name


class ProxifierInstance(models.Model):
    class Meta:
        app_label = 'Proxifier'

    term1 = models.CharField(max_length=999, blank=True, null=True)
    term2 = models.CharField(max_length=999, blank=True, null=True)
    end_date = models.DateField()
    visit_number = models.IntegerField()

    def __unicode__(self):
        return self.term1 + " " + self.term2