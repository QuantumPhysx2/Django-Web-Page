# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-14 05:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_file', '0006_auto_20180514_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(help_text='Weekly Income of Employee', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]