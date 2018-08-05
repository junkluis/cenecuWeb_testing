# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^adminIndex/$', views.index , name = 'index'),
	url(r'^eliminarCurso/(?P<pk>[0-9]+)$', views.eliminar_curso, name='eliminar_curso'),
	url(r'^login$', views.iniciar_sesion, name='iniciar_sesion'),
	url(r'^editarCurso/(?P<pk>[0-9]+)', views.editar_curso, name='editar_curso'),
	url(r'^nuevoCurso/$',views.nuevo_curso, name='nuevo_curso' ),

]




