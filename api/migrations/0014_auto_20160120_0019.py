# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 00:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20160120_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nseargv',
            options={'ordering': ['argv']},
        ),
    ]
