# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inclass_server', '0005_group_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(max_length=200, verbose_name='chave')),
                ('value', models.CharField(max_length=200, verbose_name='valor')),
            ],
            options={
                'db_table': 'system_config',
                'verbose_name': 'configura\xe7\xe3o do sistemas',
                'verbose_name_plural': 'configura\xe7\xf5es do sistema',
            },
        ),
    ]