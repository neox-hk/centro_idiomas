# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-03 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0042_auto_20170403_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='numero_consignacion',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='numero_consignacion',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
