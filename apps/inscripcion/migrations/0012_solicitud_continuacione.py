# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_academico', '0010_auto_20170310_1651'),
        ('inscripcion', '0011_auto_20170310_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud_Continuacione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmacion', models.BooleanField()),
                ('ciclo_academico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Ciclo')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Persona')),
                ('pre_curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Curso')),
            ],
        ),
    ]
