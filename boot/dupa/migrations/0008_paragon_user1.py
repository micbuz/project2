# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dupa', '0007_auto_20170118_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragon',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
