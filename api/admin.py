#!CenecuWeb/api/admin.py
"""Modelos registrados en el lado del administrador"""

from django.contrib import admin
from .models import Horario, Curso, Profesor, CursoProfesor, Area, Anuncio
from .models import Frase, GoalsList, AreaInteres, UsuarioRol, Nota
from .models import ContenidoCompartido, RegistroUsuarioCurso, Telefonos


admin.site.register(Horario)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(CursoProfesor)
admin.site.register(Area)
admin.site.register(Anuncio)
admin.site.register(Frase)
admin.site.register(GoalsList)
admin.site.register(AreaInteres)
admin.site.register(UsuarioRol)
admin.site.register(Nota)
admin.site.register(ContenidoCompartido)
admin.site.register(RegistroUsuarioCurso)
admin.site.register(Telefonos)
