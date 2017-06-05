from __future__ import unicode_literals
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.db import models


# ---------------------------------------------------------------------------- #
#
# Client Report Instance
class Client(models.Model):
    class Meta:
        app_label = 'Core'
    DNI = models.CharField(max_length=999, blank=True)
    name = models.CharField(max_length=999, blank=True)
    address = models.CharField(max_length=999, blank=True)
    telephone = models.CharField(max_length=999, blank=True)
    email = models.CharField(max_length=999, blank=True)
    legalitas_id = models.CharField(max_length=999, blank=True)

    def __unicode__(self):
        return self.name


# ---------------------------------------------------------------------------- #
#
# BusinessReport Instance
class Business(models.Model):
    class Meta:
        app_label = 'Core'
    brand = models.CharField(max_length=999, blank=True)
    client = models.ForeignKey(Client)

    NIF = models.CharField(max_length=999, blank=True)
    owner_name = models.CharField(max_length=999, blank=True)
    business_address = models.CharField(max_length=999, blank=True)
    business_telephone = models.CharField(max_length=999, blank=True)
    business_email = models.CharField(max_length=999, blank=True)
    web_url = models.CharField(max_length=999, blank=True)
    sector = models.CharField(max_length=999, blank=True)

    def get_mention_count(self):
        return self.mention_set.count()

    def __unicode__(self):
        return self.brand + "_" + str(self.id)


# ---------------------------------------------------------------------------- #
#
# Batch Instance
class Batch(models.Model):
    class Meta:
        app_label = 'Core'
    client = models.ForeignKey(Client)
    business = models.ForeignKey(Business,  blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    product_type = models.CharField(max_length=999, blank=True)
    product_instance = models.CharField(max_length=999, blank=True)
    status = models.CharField(max_length=30, default="pending")

    def __unicode__(self):
        return str(self.id)


# ---------------------------------------------------------------------------- #
#
# Brand Report Instance
class BrandReportInstance(models.Model):
    class Meta:
        app_label = 'Core'

    business_name = models.CharField(max_length=999, blank=True, null=True)
    tripadvisor_url = models.CharField(max_length=999, blank=True, null=True)
    google_url = models.CharField(max_length=999, blank=True, null=True)
    facebook_url = models.CharField(max_length=999, blank=True, null=True)

    def __unicode__(self):
        return str(self.business_name)


# ---------------------------------------------------------------------------- #
#
# General mentions
class Mention(models.Model):
    class Meta:
        app_label = 'ReportGenerator'

    mention_type_list = (
        ('twitter', 'TWITTER'),
        ('facebook', 'FACEBOOK'),
        ('instagram', 'INSTAGRAM'),
        ('forum', 'FORUM'),
        ('news', 'NEWS'),
        ('blog', 'BLOG'),
        ('video', 'VIDEO'),
        ('google', 'GOOGLE'),
        ('general', 'GENERAL'),
        ('trip', 'TRIP ADVISOR'),
    )

    business = models.ForeignKey(Business)
    social_network = models.CharField(max_length=200, choices=mention_type_list)
    sentiment = models.CharField(max_length=200, blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.TextField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    user_pic = models.TextField(blank=True, null=True)
    web_url = models.TextField(blank=True, null=True)
    impact = models.CharField(max_length=200, blank=True, null=True)
    impressions = models.CharField(max_length=200, blank=True, null=True)
    stars = models.CharField(max_length=200, blank=True, null=True)

    #  Just for twitter
    retweets = models.CharField(max_length=200, blank=True, null=True)
    followers = models.CharField(max_length=200, blank=True, null=True)
    following = models.CharField(max_length=200, blank=True, null=True)
    twitter_id = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.content) or u''
