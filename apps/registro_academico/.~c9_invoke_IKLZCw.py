from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#Ciclos Academicos
class Ciclo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self):
        return '{}'.format(self.nombre)
        
    def __unicode__(self):
        return self.nombre
    
#Sedes Academicos    
class Sede(models.Model):
    nombre = models.CharField(max_length=15)
    direccion = models.CharField(max_length=20)
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def __unicode__(self):
        return self.nombre

#Idioma (Principal)
class Idioma(models.Model):
    nombre = models.CharField(max_length=15)
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def __unicode__(self):
        return self.nombre

#Nivel (A.1.1-A.1.2-B.1.1-B.1.2)
class Nivel(models.Model):
    nombre = models.CharField(max_length=15)
    pre_requisito = models.ManyToManyField("self", blank=True)
    
    def __str__(self):
        return '{}'.format(self.nombre)

#Jornada (Horarios)
class Jornada(models.Model):
    descripcion_jornada = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.descripcion_jornada)
        
    def __unicode__(self):
        return self.descripcion_jornada

#Edad (Mayor/Menor de edad)
class Edad(models.Model):
    descripcion_edad = models.CharField(max_length=20)
    
    def __str__(self):
        return '{}'.format(self.descripcion_edad)
        
    def __unicode__(self):
        return self.descripcion_edad
    
#Tipo de Identificacion (TI-CC)
class Identificacion(models.Model):
    tipo = models.CharField(max_length=20)    
    clave = models.CharField(max_length=4)
    
    def __str__(self):
        return '{}'.format(self.clave)
        
    def __unicode__(self):
        return self.clave
    
#Discapacidad
class Discapacidad(models.Model):
    tipo = models.CharField(max_length=20)    
    
    def __str__(self):
        return '{}'.format(self.tipo)
        
    def __unicode__(self):
        return self.tipo
        
class Curso(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    ciclo = models.ForeignKey(Ciclo,null=True,blank=True)
    sede = models.ForeignKey(Sede,null=True,blank=True)
    idioma = models.ForeignKey(Idioma,null=True,blank=True)
    nivel = models.ForeignKey(Nivel,null=True,blank=True)
    jornada = models.ForeignKey(Jornada,null=True,blank=True)
    edad = models.ForeignKey(Edad,null=True,blank=True)
    
    def __str__(self):
        return '{} {} {} {}'.format(self.idioma, self.sede, self.nivel, self.jornada)
        
    def __unicode__(self):
        return self.nombre


from ..inscripcion.models import Persona

class Matricula(models.Model):
    curso = models.ForeignKey(Curso,null=True,blank=True)
    persona = models.ForeignKey(Persona,null=True,blank=True)
    nota = models.IntegerField()

    edad = models.ForeignKey(Edad,null=True,blank=True)
    fecha_examen = models.DateField(blank=True)
    sede = models.ForeignKey(Sede,null=True,blank=True)
    idioma = models.ForeignKey(Idioma,null=True,blank=True)
    edad = models.ForeignKey(Edad,null=True,blank=True)
    salon = models.CharField(max_length=50)
    numero_estudiantes = models.IntegerField()
    
    def __str__(self):
        return '{} {} {}'.format(self.fecha_examen, self.sede, self.idioma, self.edad, self.edad)
        
    def __unicode__(self):
        return self.salon
    