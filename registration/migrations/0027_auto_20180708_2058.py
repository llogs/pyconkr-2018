# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-08 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0026_auto_20180607_1241'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set([]),
        ),
    ]
