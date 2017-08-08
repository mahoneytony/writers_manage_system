# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_model',
            name='abstract',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order_model',
            name='account',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='assign_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='client_deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='client_num_of_order',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='details',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='files',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='format',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='number_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='number_of_sources',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='order_file',
            field=models.FileField(blank=True, upload_to='order_files/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='order_model',
            name='paper_type',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='problems',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='questions',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='real_time_deadline',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='send_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='slieds',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='spaced',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='subject',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='topic',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='words_min',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='writer_deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_model',
            name='writer_email',
            field=models.EmailField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='writer_number',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='order_model',
            name='writer_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
