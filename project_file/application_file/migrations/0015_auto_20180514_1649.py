# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-14 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_file', '0014_auto_20180514_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(blank=True, help_text='Customer Email', max_length=254),
        ),
    ]
