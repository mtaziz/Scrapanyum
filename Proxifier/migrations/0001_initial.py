# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProxifierAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('user_name', models.CharField(max_length=30, null=True, blank=True)),
                ('password', models.CharField(max_length=30, null=True, blank=True)),
                ('phone', models.CharField(max_length=30, null=True, blank=True)),
                ('alt_mail', models.CharField(max_length=30, null=True, blank=True)),
                ('browser', models.CharField(max_length=30, null=True, blank=True)),
                ('user_agent', models.TextField(null=True, blank=True)),
                ('plugin_list', models.CharField(max_length=300, null=True, blank=True)),
                ('screen_width', models.CharField(max_length=300, null=True, blank=True)),
                ('screen_height', models.CharField(max_length=300, null=True, blank=True)),
                ('profile_file', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProxifierInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term1', models.CharField(max_length=999, null=True, blank=True)),
                ('term2', models.CharField(max_length=999, null=True, blank=True)),
                ('end_date', models.DateField()),
                ('visit_number', models.IntegerField()),
            ],
        ),
    ]
