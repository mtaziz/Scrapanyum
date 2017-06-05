# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=999)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=50)),
                ('likes', models.CharField(max_length=50)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('user_pic', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200, null=True, editable=False, blank=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScraperWebsites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
                ('scraper_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripAdvisorBusiness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_reviews', models.CharField(max_length=200)),
                ('number_of_negative', models.CharField(max_length=200, null=True, blank=True)),
                ('percentage_negative', models.CharField(max_length=200, null=True, blank=True)),
                ('restaurant_name', models.CharField(max_length=200)),
                ('restaurant_url', models.CharField(max_length=200)),
                ('stars', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200, null=True, blank=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to='dynamic_scraper.SchedulerRuntime', null=True)),
                ('scraper_website', models.ForeignKey(editable=False, to='Scraper.ScraperWebsites', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripAdvisorReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('user_pic', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200, null=True, editable=False, blank=True)),
                ('business', models.ForeignKey(related_name='reviews', blank=True, editable=False, to='Scraper.TripAdvisorBusiness', null=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to='dynamic_scraper.SchedulerRuntime', null=True)),
                ('scraper_website', models.ForeignKey(editable=False, to='Scraper.ScraperWebsites')),
            ],
        ),
        migrations.AddField(
            model_name='googlereview',
            name='scraper_website',
            field=models.ForeignKey(editable=False, to='Scraper.ScraperWebsites'),
        ),
        migrations.AddField(
            model_name='facebookreview',
            name='scraper_website',
            field=models.ForeignKey(editable=False, to='Scraper.ScraperWebsites'),
        ),
    ]
