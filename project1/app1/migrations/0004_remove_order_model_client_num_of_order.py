# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20170207_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_model',
            name='client_num_of_order',
        ),
    ]
