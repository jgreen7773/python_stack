# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-14 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_auto_20190914_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninjas',
            name='dojo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending_dojo', to='dojo_ninjas_app.dojos'),
        ),
    ]
