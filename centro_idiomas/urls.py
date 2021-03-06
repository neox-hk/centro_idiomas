# -*- coding: utf-8 -*-
"""centro_idiomas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth.views import login
from apps.usuario.views import inicio_sesion, index,bienvenido

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inscripcion/', include('apps.inscripcion.urls', namespace="inscripcion")),
    url(r'^usuarios/', include('apps.usuario.urls', namespace="usuario")),
    
    url(r'^$',inicio_sesion, name="login"),
    url(r'^index/',index, name='index'),
    url(r'^bienvenido/',bienvenido, name='bienvenido'),
]
