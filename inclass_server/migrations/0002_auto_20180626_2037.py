# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inclass_server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='external_code',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='api_token',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='is_new_password',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='absence',
            unique_together=set([('lecture', 'student')]),
        ),
    ]