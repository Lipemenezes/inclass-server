# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inclass_server', '0003_auto_20180626_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
    ]
