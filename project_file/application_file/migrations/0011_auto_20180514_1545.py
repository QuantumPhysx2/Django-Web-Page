# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-14 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_file', '0010_auto_20180514_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='vehicle_id',
            field=models.ForeignKey(help_text='Assigned Vehicle', on_delete=django.db.models.deletion.CASCADE, to='application_file.Vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='drivetrain',
            field=models.CharField(help_text='FWD/RWD/AWD/2WD/4WD', max_length=3),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.CharField(help_text='Name of Company Maker', max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(help_text='Name of Vehicle', max_length=100),
        ),
    ]
