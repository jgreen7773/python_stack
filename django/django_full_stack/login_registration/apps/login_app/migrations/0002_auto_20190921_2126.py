# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-21 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='user1',
        ),
    ]