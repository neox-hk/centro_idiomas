# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0015_inscripcion_examen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='num_identificacion',
            field=models.BigIntegerField(),
        ),
    ]
