# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scraper', '0002_auto_20170523_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripadvisorbusiness',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='tripadvisorbusiness',
            name='scraper_website',
        ),
        migrations.RemoveField(
            model_name='tripadvisorreview',
            name='business',
        ),
        migrations.DeleteModel(
            name='TripAdvisorBusiness',
        ),
    ]
