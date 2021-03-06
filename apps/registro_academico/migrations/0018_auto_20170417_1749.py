# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_academico', '0017_auto_20170411_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Franja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Semana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='franja',
            name='dia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Semana'),
        ),
    ]
