import datetime
import json
import operator
import os
import re

import requests
import tweepy
from instagram.client import InstagramAPI
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Core.models import Mention
from Scraper.models import ScraperWebsites
from Scraper.models import GoogleReview
from Scraper.models import TripAdvisorReview


def scrape_websites(report, business):
    try:
        # Create website for trip advisor
        print "Scraper de Trip Advisor"
        scraper_website_trip = ScraperWebsites(
            name=business.brand,
            url=report.tripadvisor_url,
            scraper_id=3,
            scraper_runtime_id=1
        )
        scraper_website_trip.save()
        spider_call = "scrapy crawl tripadvisor_scraper -a id=%s -a do_action=yes" % scraper_website_trip.id
        os.system(spider_call)

        # Transform reviews to mentions
        print "Transformando datos de TripAdvisor en menciones"
        trip_review_array = TripAdvisorReview.objects.all()
        for gr in trip_review_array:
            stars = "3"
            sentiment = "neutral"
            if gr.stars:
                stars = re.findall(r"([0-9])", gr.stars)[0]
                if stars == "4" or stars == "5":
                    sentiment = "positive"
                elif stars == "1" or stars == "2":
                    sentiment = "negative"
                else:
                    sentiment = "neutral"

            m = Mention(
                business=business,
                social_network=r"trip",
                content=gr.content.encode("utf-8"),
                user=gr.user.encode("utf-8"),
                title=gr.title.encode("utf-8"),
                date=gr.date.encode("utf-8"),
                stars=stars.encode("utf-8"),
                sentiment=sentiment.encode("utf-8")
            )
            m.save()

        trip_review_array.delete()
    except Exception as e:
        print e

    try:
        # Create website for google reviews
        print report.google_url
        scraper_website_google = ScraperWebsites(
            name=business.brand,
            url=report.google_url,
            # url="https://www.google.com",
            scraper_id=2,
            scraper_runtime_id=1
        )
        # scrape trip google
        scraper_website_google.save()
        spider_call = "scrapy crawl google_review_scraper -a id=%s -a do_action=yes" % scraper_website_google.id
        os.system(spider_call)

        # Transform reviews to mentions
        print "Transformando datos de GoogleReviews en menciones"
        google_review_array = GoogleReview.objects.all()
        for gr in google_review_array:

            s = re.findall(r"([0-9],[0-9])", gr.stars)[0]
            clean_stars = s[0].replace(',0', '0')
            m = Mention(
                business=business,
                social_network="google",
                user=gr.user,
                date=gr.date,
                stars=clean_stars,
                content=gr.content,
            )
            m.save()
        google_review_array.delete()
    except Exception as e:
        print e