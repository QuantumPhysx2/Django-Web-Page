# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-14 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_file', '0012_customer_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(default='@gmail.com', help_text='Customer Email', max_length=254),
        ),
    ]
