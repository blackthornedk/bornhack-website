# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_creditnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='refunded',
            field=models.BooleanField(default=False, help_text='Whether this order has been refunded.', verbose_name='Refunded?'),
        ),
    ]
