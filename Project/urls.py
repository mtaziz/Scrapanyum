from django.conf.urls import include, url
from django.contrib import admin

import Core.urls
import Scraper.urls
import Proxifier.urls


admin.autodiscover()

urlpatterns = [
    url(r'', include(Core.urls)),
    url(r'', include(Scraper.urls)),
    url(r'', include(Proxifier.urls)),


    url(r'^admin/', include(admin.site.urls)),
]
