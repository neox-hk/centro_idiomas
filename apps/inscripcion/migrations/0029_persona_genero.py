# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_academico', '0011_genero'),
        ('inscripcion', '0028_auto_20170324_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Genero'),
        ),
    ]
