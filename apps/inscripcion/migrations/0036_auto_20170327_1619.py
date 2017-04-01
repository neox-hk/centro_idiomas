# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-27 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0035_auto_20170327_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_continuacione',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Idioma'),
        ),
        migrations.AlterField(
            model_name='solicitud_continuacione',
            name='nivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Nivel'),
        ),
        migrations.AlterField(
            model_name='solicitud_continuacione',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Persona'),
        ),
        migrations.AlterField(
            model_name='solicitud_continuacione',
            name='pre_curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Curso'),
        ),
    ]