# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140),
        ),
    ]
