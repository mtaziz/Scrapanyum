from __future__ import unicode_literals
from dynamic_scraper.spiders.django_checker import DjangoChecker
# from Scraper.models import Article
from Scraper.models import TripAdvisorReview


# class ArticleChecker(DjangoChecker):
#
#     name = 'article_checker'
#
#     def __init__(self, *args, **kwargs):
#         self._set_ref_object(Article, **kwargs)
#         self.scraper = self.ref_object.news_website.scraper
#         self.scheduler_runtime = self.ref_object.checker_runtime
#         super(ArticleChecker, self).__init__(self, *args, **kwargs)


class TripAdvisorReviewChecker(DjangoChecker):
    name = 'article_checker'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(TripAdvisorReview, **kwargs)
        self.scraper = self.ref_object.Scraper.scraper
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(TripAdvisorReviewChecker, self).__init__(self, *args, **kwargs)