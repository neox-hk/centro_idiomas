# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-10 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro_academico', '0008_matricula_ciclo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='ciclo',
        ),
    ]
