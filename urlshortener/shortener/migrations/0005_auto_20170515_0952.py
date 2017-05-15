# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20170106_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigurl',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bigurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]