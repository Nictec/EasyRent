# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0032_auto_20170223_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='Equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='storage.Equipment'),
        ),
    ]
