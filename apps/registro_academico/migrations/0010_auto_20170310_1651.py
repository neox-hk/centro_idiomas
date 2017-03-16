# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-10 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_academico', '0009_remove_matricula_ciclo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nivel',
            name='pre_requisito',
        ),
        migrations.AddField(
            model_name='nivel',
            name='pre_requisito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Nivel'),
        ),
    ]