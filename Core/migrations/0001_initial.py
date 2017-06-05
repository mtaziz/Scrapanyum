# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legalitas_batch', models.CharField(max_length=999, blank=True)),
                ('start', models.DateField(null=True, blank=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('product_type', models.CharField(max_length=999, blank=True)),
                ('product_instance', models.CharField(max_length=999, blank=True)),
                ('status', models.CharField(default='pending', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=999, blank=True)),
                ('NIF', models.CharField(max_length=999, blank=True)),
                ('owner_name', models.CharField(max_length=999, blank=True)),
                ('business_address', models.CharField(max_length=999, blank=True)),
                ('business_telephone', models.CharField(max_length=999, blank=True)),
                ('business_email', models.CharField(max_length=999, blank=True)),
                ('web_url', models.CharField(max_length=999, blank=True)),
                ('sector', models.CharField(max_length=999, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DNI', models.CharField(max_length=999, blank=True)),
                ('name', models.CharField(max_length=999, blank=True)),
                ('address', models.CharField(max_length=999, blank=True)),
                ('telephone', models.CharField(max_length=999, blank=True)),
                ('email', models.CharField(max_length=999, blank=True)),
                ('legalitas_id', models.CharField(max_length=999, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='client',
            field=models.ForeignKey(to='Core.Client'),
        ),
        migrations.AddField(
            model_name='batch',
            name='business',
            field=models.ForeignKey(blank=True, to='Core.Business', null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='client',
            field=models.ForeignKey(to='Core.Client'),
        ),
    ]
