# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-17 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RTV_app', '0002_auto_20190917_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='net6',
            field=models.ManyToManyField(related_name='provider', to='RTV_app.Show'),
        ),
    ]
