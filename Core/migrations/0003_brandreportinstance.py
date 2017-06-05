# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_remove_batch_legalitas_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandReportInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_name', models.CharField(max_length=999, null=True, blank=True)),
                ('tripadvisor_url', models.CharField(max_length=999, null=True, blank=True)),
                ('google_url', models.CharField(max_length=999, null=True, blank=True)),
                ('facebook_url', models.CharField(max_length=999, null=True, blank=True)),
            ],
        ),
    ]
