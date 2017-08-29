# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0002_auto_20170819_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='player',
        ),
        migrations.RemoveField(
            model_name='song',
            name='id',
        ),
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]