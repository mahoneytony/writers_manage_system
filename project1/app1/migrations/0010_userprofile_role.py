# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_tender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(default='writer', max_length=30),
        ),
    ]
