# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 03:04
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nse',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=(('auth', 'auth'), ('broadcast', 'broadcast'), ('brute', 'brute'), ('default', 'default'), ('discovery', 'discovery'), ('dos', 'dos'), ('exploit', 'exploit'), ('external', 'external'), ('fuzzer', 'fuzzer'), ('intrusive', 'intrusive'), ('malware', 'malware'), ('safe', 'safe'), ('version', 'version'), ('vuln', 'vuln'))),
        ),
        migrations.DeleteModel(
            name='NseCategory',
        ),
    ]
