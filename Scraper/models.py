from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from Core.models import Client


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, ScraperWebsites):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()

    if isinstance(instance, TripAdvisorReview):
        if instance.checker_runtime:
            instance.checker_runtime.delete()


pre_delete.connect(pre_delete_handler)


class ScraperWebsites(models.Model):
    class Meta:
        app_label = 'Scraper'
    name = models.CharField(max_length=999)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


# ---------------------------------------------------------------------------- #
#
# TRIP ADVISOR
# class TripAdvisorBusiness(models.Model):
#     class Meta:
#         app_label = 'Scraper'
#     number_of_reviews = models.CharField(max_length=200)
#     number_of_negative = models.CharField(max_length=200, blank=True, null=True)
#     percentage_negative = models.CharField(max_length=200, blank=True, null=True)
#     restaurant_name = models.CharField(max_length=200)
#     restaurant_url = models.CharField(max_length=200)
#     stars = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     telephone = models.CharField(max_length=200, blank=True, null=True)
#
#     checker_runtime = models.ForeignKey(SchedulerRuntime, editable=False, blank=True, null=True,
#                                         on_delete=models.SET_NULL)
#     scraper_website = models.ForeignKey(ScraperWebsites, editable=False, null=True)
#
#     def get_reviews(self):
#         return self.reviews.all()
#
#     def get_reviews_by_stars(self, stars):
#         return self.reviews.filter(stars=stars)[:5]
#
#
# class TripAdvisorBusinessItem(DjangoItem):
#     class Meta:
#         app_label = 'Scraper'
#     django_model = TripAdvisorBusiness


class TripAdvisorReview(models.Model):
    class Meta:
        app_label = 'Scraper'
    stars = models.CharField(max_length=200)
    title = models.TextField()
    content = models.TextField()
    date = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    user_pic = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, editable=False, blank=True, null=True)

    checker_runtime = models.ForeignKey(SchedulerRuntime, editable=False, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    scraper_website = models.ForeignKey(ScraperWebsites, editable=False)
    # business = models.ForeignKey(TripAdvisorBusiness, editable=False, blank=True, null=True, related_name="reviews")



class TripAdvisorReviewItem(DjangoItem):
    class Meta:
        app_label = 'Scraper'
    django_model = TripAdvisorReview


# ---------------------------------------------------------------------------- #
#
# FACEBOOK
class FacebookReview(models.Model):
    class Meta:
        app_label = 'Scraper'

    stars = models.CharField(max_length=200)
    user = models.CharField(max_length=999)
    content = models.TextField()
    date = models.CharField(max_length=50)
    likes = models.CharField(max_length=50)
    checker_runtime = models.ForeignKey(SchedulerRuntime, editable=False, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    scraper_website = models.ForeignKey(ScraperWebsites, editable=False)


class FacebookReviewItem(DjangoItem):
    class Meta:
        app_label = 'Scraper'
    django_model = FacebookReview


# ---------------------------------------------------------------------------- #
#
# GOOGLE
class GoogleReview(models.Model):
    class Meta:
        app_label = 'Scraper'
    stars = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    user_pic = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, editable=False, blank=True, null=True)

    checker_runtime = models.ForeignKey(SchedulerRuntime, editable=False, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    scraper_website = models.ForeignKey(ScraperWebsites, editable=False)


class GoogleReviewItem(DjangoItem):
    class Meta:
        app_label = 'Scraper'
    django_model = GoogleReview
