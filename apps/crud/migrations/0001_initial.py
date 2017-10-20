# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('plan', models.CharField(max_length=255)),
                ('startDate', models.DateField(null=True)),
                ('endDate', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(default='000', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='crud.User'),
        ),
        migrations.AddField(
            model_name='trip',
            name='otherUsers',
            field=models.ManyToManyField(related_name='attachedtrips', to='crud.User'),
        ),
    ]
