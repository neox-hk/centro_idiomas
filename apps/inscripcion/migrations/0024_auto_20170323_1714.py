# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-23 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0023_auto_20170323_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email_acudiente',
            field=models.EmailField(default='prueba@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono_acudiente',
            field=models.BigIntegerField(default=3163431036),
            preserve_default=False,
        ),
    ]
