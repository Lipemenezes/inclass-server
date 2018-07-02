# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Frutinha(models.Model):
    name = models.CharField(max_length=200, verbose_name='name', unique=True)

    def to_dict(self):
        return {
            'name': self.name
        }

    class Meta:
        db_table = 'frutinha'
        verbose_name = 'frutinha'
        verbose_name_plural = 'frutinhas'