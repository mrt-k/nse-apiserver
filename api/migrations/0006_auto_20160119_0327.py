# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160119_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nse',
            name='argvs',
        ),
        migrations.AddField(
            model_name='nse',
            name='argvs',
            field=models.ManyToManyField(to='api.NseArgv'),
        ),
    ]
