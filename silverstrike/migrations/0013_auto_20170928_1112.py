# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0012_auto_20170928_1103'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Journal',
            new_name='Transaction',
        ),
    ]