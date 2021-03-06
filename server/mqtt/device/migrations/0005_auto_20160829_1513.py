# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 15:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_auto_20160819_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='last_seen',
        ),
        migrations.AddField(
            model_name='device',
            name='last_offline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last time the device went offline'),
        ),
        migrations.AddField(
            model_name='operation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 29, 15, 13, 17, 719211)),
            preserve_default=False,
        ),
    ]
