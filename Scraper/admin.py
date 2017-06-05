from __future__ import unicode_literals

from django.contrib import admin

from Scraper.models import FacebookReview
from Scraper.models import ScraperWebsites
from Scraper.models import TripAdvisorReview
from Scraper.models import GoogleReview


# ---------------------------------------------------------------------------- #
#
# WEBSITE
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scraper')
    list_display_links = ('name',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


admin.site.register(ScraperWebsites, WebsiteAdmin)


# ---------------------------------------------------------------------------- #
#
# TRIP ADVISOR
class TripAdvisorReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user',)
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


admin.site.register(TripAdvisorReview, TripAdvisorReviewAdmin)


# ---------------------------------------------------------------------------- #
#
# FACEBOOK
class FacebookReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'user')
    list_display_links = ('content',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


admin.site.register(FacebookReview, FacebookReviewAdmin)


# ---------------------------------------------------------------------------- #
#
# GOOGLE
class GoogleReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'user')
    list_display_links = ('content',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


admin.site.register(GoogleReview, GoogleReviewAdmin)

