# -*- coding: utf-8 -*-
# Stage 2 Update (Python 3)
from __future__ import absolute_import
from __future__ import unicode_literals

import json
import logging
import time

from dynamic_scraper.spiders.django_spider import DjangoSpider
from jsonpath_rw import parse
from jsonpath_rw.lexer import JsonPathLexerError
from scrapy.exceptions import CloseSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from selenium import webdriver

from Scraper.models import GoogleReview, GoogleReviewItem
from Scraper.models import ScraperWebsites
from Scraper.models import TripAdvisorReview, TripAdvisorReviewItem


# TRIP ADVISOR REVIEWS
class TripAdvisorReviewSpider(DjangoSpider):
    name = 'tripadvisor_scraper'

    def __init__(self, business_url='', *args, **kwargs):
        self._set_ref_object(ScraperWebsites, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        # set items
        self.scraped_obj_class = TripAdvisorReview
        self.scraped_obj_item_class = TripAdvisorReviewItem

        super(TripAdvisorReviewSpider, self).__init__(self, *args, **kwargs)



# ---------------------------------------------------------------------------- #
#
# GOOGLE REVIEWS EXAMPLE
class GoogleReviewSpider(DjangoSpider):
    name = 'google_review_scraper'

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.Firefox()
        self._set_ref_object(ScraperWebsites, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        # set items
        self.scraped_obj_class = GoogleReview
        self.scraped_obj_item_class = GoogleReviewItem

        super(GoogleReviewSpider, self).__init__(self, *args, **kwargs)

    def parse(self, response):
        self.scrape_url = self.ref_object.url
        # self.scrape_url = "https://www.google.es/search?q=puerto+blanco+calpe&oq=puerto+blanco+calpe&aqs=chrome..69i57j69i61j69i60l2j0l2.2465j0j7&sourceid=chrome&ie=UTF-8#q=voraz+sevilla&lrd=0xd126c389f4da40b:0x72079bb2705d6b12,1,"
        self.driver.get(self.scrape_url)

        time.sleep(3)
        # base_elem = self.scraper.get_base_elem()

        for _ in range(5):
            time.sleep(3)
            self.driver.execute_script("document.getElementsByClassName('review-dialog-list')[0].scrollBy(0,3000)")

            time.sleep(3)

            base_elem = self.scraper.get_base_elem()

        if self.scraper.get_main_page_rpt().content_type == 'J':
            json_resp = json.loads(response.body_as_unicode())
            try:
                jsonpath_expr = parse(base_elem.x_path)
            except JsonPathLexerError:
                raise CloseSpider("JsonPath for base elem could not be processed!")
            base_objects = [match.value for match in jsonpath_expr.find(json_resp)]
            if len(base_objects) > 0:
                base_objects = base_objects[0]
        else:
            # reloads the page source and grabs the elements from xpath from there
            source = self.driver.page_source
            sel = Selector(text=source)
            base_objects = sel.xpath(base_elem.x_path)

        if (len(base_objects) == 0):
            self.log("No base objects found!", logging.ERROR)

        if (self.conf['MAX_ITEMS_READ']):
            items_left = min(len(base_objects), self.conf['MAX_ITEMS_READ'] - self.items_read_count)
            base_objects = base_objects[0:items_left]

        for obj in base_objects:
            item_num = self.items_read_count + 1
            self.tmp_non_db_results[item_num] = {}
            self.log("Starting to crawl item {i} from page {p}.".format(i=str(item_num),
                                                                        p=str(response.request.meta['page'])),
                     logging.INFO)
            item = self.parse_item(response, obj, 'MP', item_num)

            if item:
                only_main_page_idfs = True
                idf_elems = self.scraper.get_id_field_elems()
                for idf_elem in idf_elems:
                    if idf_elem.request_page_type != 'MP':
                        only_main_page_idfs = False

                is_double = False
                if only_main_page_idfs and self.conf['DO_ACTION']:
                    item, is_double = self._check_for_double_item(item)

                cnt_sue_detail = self.scraper.get_standard_update_elems_from_detail_pages().count()
                cnt_detail_scrape = self.scraper.get_from_detail_pages_scrape_elems().count()

                if self.scraper.get_detail_page_url_elems().count() == 0 or \
                        (is_double and cnt_sue_detail == 0) or cnt_detail_scrape == 0:
                    self.non_db_results[id(item)] = self.tmp_non_db_results[item_num].copy()
                    # item['city'] = self.city
                    yield item
                else:
                    # self.run_detail_page_request()
                    url_elems = self.scraper.get_detail_page_url_elems()
                    for url_elem in url_elems:
                        if not url_elem.scraped_obj_attr.save_to_db:
                            url = self.tmp_non_db_results[item_num][url_elem.scraped_obj_attr.name]
                            url = self._replace_detail_page_url_placeholders(url, item, item_num)
                            self.tmp_non_db_results[item_num][url_elem.scraped_obj_attr.name] = url
                        else:
                            url = item[url_elem.scraped_obj_attr.name]
                            url = self._replace_detail_page_url_placeholders(url, item, item_num)
                            item[url_elem.scraped_obj_attr.name] = url
                        rpt = self.scraper.get_rpt_for_scraped_obj_attr(url_elem.scraped_obj_attr)
                        kwargs = self.dp_request_kwargs[rpt.page_type].copy()
                        if 'meta' not in kwargs:
                            kwargs['meta'] = {}
                        kwargs['meta']['item'] = item
                        kwargs['meta']['from_page'] = rpt.page_type
                        kwargs['meta']['item_num'] = item_num
                        if url_elem == url_elems[len(url_elems) - 1]:
                            kwargs['meta']['last'] = True
                        else:
                            kwargs['meta']['last'] = False
                        self._set_meta_splash_args()
                        # logging.info(str(kwargs))
                        if rpt.request_type == 'R':
                            yield Request(url, callback=self.parse_item, method=rpt.method,
                                          dont_filter=rpt.dont_filter,
                                          **kwargs)
                        else:
                            yield FormRequest(url, callback=self.parse_item, method=rpt.method,
                                              formdata=self.dp_form_data[rpt.page_type],
                                              dont_filter=rpt.dont_filter,
                                              **kwargs)
            else:
                self.log("Item could not be read!", logging.ERROR)


