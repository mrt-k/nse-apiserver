# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 03:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160119_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nseargv',
            name='script',
        ),
    ]