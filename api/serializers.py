#!CenecuWeb/api/serializers.py
"""Serializadores a Json"""

from rest_framework import serializers
from .models import Horario, Curso, Profesor, CursoProfesor, Area, Anuncio
from .models import Frase, GoalsList, AreaInteres, UsuarioRol, Nota
from .models import ContenidoCompartido, RegistroUsuarioCurso, Telefonos

class HorarioSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Horario
        fields = ('pk', 'curso_id', 'dia', 'hora_inicio',
                  'minutos_inicio', 'hora_fin', 'minutos_fin')


class CursoSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Curso
        fields = ('pk', 'nombre', 'descripcion', 'pensum',
                  'duracion_cant', 'duracion_tipo', 'costo',
                  'img_curso', 'area_estudio', 'estado', 'fecha_creado')
        read_only_fields = ['fecha_creado']


class ProfesorSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Profesor
        fields = ('pk', 'nombre', 'apellido', 'titulo',
                  'img_perfil', 'frases_personal', 'biografia',
                  'area_especializacion', 'url_linkedin',
                  'curriculum', 'estado', 'fecha_creado')
        read_only_fields = ['fecha_creado']


class CursoProfesorSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = CursoProfesor
        fields = ('pk', 'curso_id', 'profesor_id')


class AreaSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Area
        fields = ('pk', 'nombre', 'descripcion',
                  'img_area', 'estado')


class AnuncioSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Anuncio
        fields = ('pk', 'descripcion', 'img_anuncio',
                  'fecha_limite', 'estado', 'fecha_creado')
        read_only_fields = ['fecha_creado']


class FraseSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Frase
        fields = ('pk', 'descripcion', 'img_frase',
                  'estado', 'fecha_creado')
        read_only_fields = ['fecha_creado']


class GoalsListSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = GoalsList
        fields = ('pk', 'usuario_id', 'curso_id',
                  'estado', 'fecha_creado')
        read_only_fields = ['fecha_creado']


class AreaInteresSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = AreaInteres
        fields = ('pk', 'usuario_id', 'area_id')


class UsuarioRolSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = UsuarioRol
        fields = ('pk', 'usuario_id', 'rol')


class NotaSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Nota
        fields = ('pk', 'titulo', 'descripcion',
                  'fecha_limite', 'notificacion',
                  'fecha_notificacion', 'usuario_id',
                  'estado', 'fecha_creado')
        read_only_fields = ['fecha_creado']


class ContenidoCompartidoSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = ContenidoCompartido
        fields = ('pk', 'curso_id', 'usuario_id',
                  'fecha_compartido', 'red_social')


class RegistroUsuarioCursoSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = RegistroUsuarioCurso
        fields = ('pk', 'curso_id', 'usuario_id',
                  'fecha_solicitud')



class TelefonosSerializer(serializers.ModelSerializer):
    """Serializador"""

    class Meta:
        """campos"""
        model = Telefonos
        fields = ('pk', 'usuario_id', 'telefonos')
