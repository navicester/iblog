# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 12:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 4, 18, 12, 21, 50, 272000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]