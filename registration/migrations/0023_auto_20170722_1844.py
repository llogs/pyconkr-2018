# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_manualpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='count_reissue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registration',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='issue_ticket',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='reissue_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
