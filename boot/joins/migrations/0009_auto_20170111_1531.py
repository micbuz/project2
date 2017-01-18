# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0008_join_ref_if'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='ref_if',
        ),
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='abra', max_length=120),
        ),
    ]