# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_order_model_times_returned_for_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rejected_orders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Order_model'),
        ),
    ]