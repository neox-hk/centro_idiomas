# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_academico', '0011_genero'),
        ('inscripcion', '0037_auto_20170327_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion_examen',
            name='nivel_sugerido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Nivel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscripcion_examen',
            name='citacion',
            field=models.ForeignKey(default=47, on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Citacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscripcion_examen',
            name='inscripcion',
            field=models.ForeignKey(default=36, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Inscripcion'),
            preserve_default=False,
        ),
    ]
