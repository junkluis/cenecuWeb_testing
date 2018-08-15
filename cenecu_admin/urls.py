# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.contrib.auth.views import login
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index , name = 'index'),
    url(r'^login/$', views.iniciar_sesion, name='iniciar_sesion'),
    url(r'^nuevoCurso/$',views.nuevo_curso, name='nuevo_curso' ),
    url(r'^crearCurso/$',views.crear_curso,name='crear_curso'),
    url(r'^editarCurso/(?P<pk>[0-9]+)', views.editar_curso, name='editar_curso'),
    url(r'^modificarCurso/$',views.modificar_curso,name='modificar_curso'),
    url(r'^eliminarCurso/(?P<pk>[0-9]+)$', views.eliminar_curso, name='eliminar_curso'),
    url(r'^listarProfesores/$', views.listar_profesores , name = 'listar_profesores'),
    url(r'^nuevoProfesor/$',views.nuevo_profesor, name='nuevo_profesor'),
    url(r'^crearProfesor/$',views.crear_profesor, name='crear_profesor' ),
    url(r'^editarProfesor/(?P<pk>[0-9]+)', views.editar_profesor, name='editar_profesor'),
    url(r'^modificarProfesor/$',views.modificar_profesor,name='modificar_profesor'),
    url(r'^eliminarProfesor/(?P<pk>[0-9]+)$', views.eliminar_profesor, name='eliminar_profesor'),
    url(r'^listarAnuncios/$', views.listar_anuncios , name = 'listar_anuncios'),
    url(r'^nuevoAnuncio/$',views.nuevo_anuncio, name='nuevo_anuncio'),
    url(r'^crearAnuncio/$',views.crear_anuncio, name='crear_anuncio' ),
    url(r'^editarAnuncio/(?P<pk>[0-9]+)', views.editar_anuncio, name='editar_anuncio'),
    url(r'^modificarAnuncio/$',views.modificar_anuncio,name='modificar_anuncio'),
    url(r'^eliminarAnuncio/(?P<pk>[0-9]+)$', views.eliminar_anuncio, name='eliminar_anuncio'),
    url(r'^listarFrases/$', views.listar_frases , name = 'listar_frases'),
    url(r'^nuevaFrase/$',views.nueva_frase, name='nueva_frase'),
    url(r'^crearFrase/$',views.crear_frase, name='crear_frase' ),
    url(r'^editarFrase/(?P<pk>[0-9]+)', views.editar_frase, name='editar_frase'),
    url(r'^modificarFrase/$',views.modificar_frase,name='modificar_frase'),
    url(r'^eliminarFrase/(?P<pk>[0-9]+)$', views.eliminar_frase, name='eliminar_frase'),
    url(r'^listarAreas/$', views.listar_areas , name = 'listar_areas'),
    url(r'^nuevaArea/$',views.nueva_area, name='nueva_area'),
    url(r'^crearArea/$',views.crear_area, name='crear_area' ),
    url(r'^editarArea/(?P<pk>[0-9]+)', views.editar_area, name='editar_area'),
    url(r'^modificarArea/$',views.modificar_area, name='modificar_area'),
    url(r'^eliminarArea/(?P<pk>[0-9]+)$', views.eliminar_area, name='eliminar_area'),
    url(r'^reportes/$',views.visualizar_reporte, name='visualizar_reporte'),
    url(r'^reporteArea/$', views.reporte_user_area_interes, name='reporte_area'),
    url(r'^reporteSolicitud/$', views.reporte_user_solicitud_registro, name='reporte_solicitud'),
    url(r'^refresh/$', views.ajaxReporteCompartido, name='ajaxReporteCompartido'),
    url(r'^seleccionCurso/$', views.visualizar_reporte_compartido, name='visualizar_reporte_compartido'),
    url(r'^seleccionCurso/(?P<pk>[0-9]+)$', views.reporte_curso_compartido, name='reporte_curso_compartido'),    
    url(r'^reporteCurso/(?P<pk>[0-9]+)$', views.reporte_curso_compartido, name='reporte_curso_compartido'),
    url(r'^exportarReporte/$',views.exportar_repo, name='exportar_reporte'),
    url(r'^logout/$',views.cerrar_sesion, name='cerrar_sesion'),
    url(r'^exportar/Reporte/(?P<reporte>[0-9]+)/(?P<curso>[0-9]+)$',views.reportes_xlsx, name='reportes_xlsx'),

    
]
