# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='creater',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='crud.User'),
        ),
    ]
