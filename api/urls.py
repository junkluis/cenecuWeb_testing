#!CenecuWeb/api/urls.py
"""Rutas del API"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HorarioView, CursoView, ProfesorView, CursoProfesorView
from .views import AreaView, AnuncioView, FraseView, GoalsListView
from .views import AreaInteresView, UsuarioRolView, NotaView, TelefonosEdit
from .views import ContenidoCompartidoView, RegistroUsuarioCursoView

from .views import TelefonosView, HorarioEdit, CursoEdit, ProfesorEdit
from .views import CursoProfesorEdit, AreaEdit, AnuncioEdit, FraseEdit
from .views import GoalsListEdit, AreaInteresEdit, UsuarioRolEdit
from .views import NotaEdit, ContenidoCompartidoEdit, RegistroUsuarioCursoEdit
from . import views

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = {
    url(r'^$', views.api_index, name="Index"),
    url(r'^Horario/$', HorarioView.as_view(), name="Horario"),
    url(r'^Curso/$', CursoView.as_view(), name="Curso"),
    url(r'^Profesor/$', ProfesorView.as_view(), name="Profesor"),
    url(r'^CursoProfesor/$', CursoProfesorView.as_view(),
        name="CursoProfesor"),
    url(r'^Area/$', AreaView.as_view(), name="Area"),
    url(r'^Anuncio/$', AnuncioView.as_view(), name="Anuncio"),
    url(r'^Frase/$', FraseView.as_view(), name="Frase"),
    url(r'^GoalsList/$', GoalsListView.as_view(), name="GoalsList"),
    url(r'^AreaInteres/$', AreaInteresView.as_view(), name="AreaInteres"),
    url(r'^UsuarioRol/$', UsuarioRolView.as_view(), name="UsuarioRol"),
    url(r'^Nota/$', NotaView.as_view(), name="Nota"),
    url(r'^ContenidoCompartido/$', ContenidoCompartidoView.as_view(),
        name="ContenidoCompartido"),
    url(r'^RegistroUsuarioCurso/$', RegistroUsuarioCursoView.as_view(),
        name="RegistroUsuarioCurso"),
    url(r'^Telefonos/$', TelefonosView.as_view(), name="Telefonos"),

    url(r'^Horario/(?P<pk>[0-9]+)/$', HorarioEdit.as_view(),
        name="HorarioEdit"),
    url(r'^Curso/(?P<pk>[0-9]+)/$', CursoEdit.as_view(),
        name="CursoEdit"),
    url(r'^Profesor/(?P<pk>[0-9]+)/$', ProfesorEdit.as_view(),
        name="ProfesorEdit"),
    url(r'^CursoProfesor/(?P<pk>[0-9]+)/$', CursoProfesorEdit.as_view(),
        name="CursoProfesorEdit"),
    url(r'^Area/(?P<pk>[0-9]+)/$', AreaEdit.as_view(), name="AreaEdit"),
    url(r'^Anuncio/(?P<pk>[0-9]+)/$', AnuncioEdit.as_view(),
        name="AnuncioEdit"),
    url(r'^Frase/(?P<pk>[0-9]+)/$', FraseEdit.as_view(), name="FraseEdit"),
    url(r'^GoalsList/(?P<pk>[0-9]+)/$', GoalsListEdit.as_view(),
        name="GoalsListEdit"),
    url(r'^AreaInteres/(?P<pk>[0-9]+)/$', AreaInteresEdit.as_view(),
        name="AreaInteresEdit"),
    url(r'^UsuarioRol/(?P<pk>[0-9]+)/$', UsuarioRolEdit.as_view(),
        name="UsuarioRolEdit"),
    url(r'^Nota/(?P<pk>[0-9]+)/$', NotaEdit.as_view(), name="NotaEdit"),
    url(r'^ContenidoCompartido/(?P<pk>[0-9]+)/$',
        ContenidoCompartidoEdit.as_view(), name="ContenidoCompartidoEdit"),
    url(r'^RegistroUsuarioCurso/(?P<pk>[0-9]+)/$',
        RegistroUsuarioCursoEdit.as_view(), name="RegistroUsuarioCursoEdit"),
    url(r'^Telefonos/(?P<pk>[0-9]+)/$', TelefonosEdit.as_view(),
        name="TelefonosEdit"),

    url(r'^Hello/$', views.hello_world, name="testOverride"),
    url(r'^loginCenecu/$', views.login_cenecu, name="login"),
    url(r'^notasUser/(?P<pk>[0-9]+)/$', views.notas_por_user,
        name="notas_por_user"),
    url(r'^borrarNota/(?P<pk>[0-9]+)/$', views.borrar_nota, name="borrar_nota"),
    url(r'^registrarUsuario/$', views.registrar_usuario,
        name="registrar_usuario"),
    url(r'^logOut/$', views.log_out, name="log_out")
}

urlpatterns = format_suffix_patterns(urlpatterns)
