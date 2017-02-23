# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20170223_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='Image',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='storeplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Shelf'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Client'),
        ),
    ]