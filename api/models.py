#!CenecuWeb/api/models.py
"""Definicion de modelos para crear la base de datos"""

from django.db import models
from django.contrib.auth.models import User


class Horario(models.Model):
    """Horarios de cursos en dia de las semanas"""

    dias_semana = (('L', 'Lunes'), ('M', 'Martes'), ('Mi', 'Miercoles'),
                   ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sabado'))

    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)
    dia = models.CharField(max_length=2, blank=False, choices=dias_semana)
    hora_inicio = models.IntegerField()
    minutos_inicio = models.IntegerField()
    hora_fin = models.IntegerField()
    minutos_fin = models.IntegerField()

    def __str__(self):
        return "{}".format(self.dia)


class Curso(models.Model):
    """Cursos de cenecu"""

    tipo_duracion = (('S', 'Semanas'), ('M', 'Meses'))
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255, blank=False)
    pensum = models.FileField(upload_to='uploads/pensums/')
    duracion_cant = models.IntegerField()
    duracion_tipo = models.CharField(max_length=1, blank=False,
                                     choices=tipo_duracion)
    costo = models.FloatField()
    img_curso = models.ImageField(upload_to='uploads/imagenes/')
    area_estudio = models.ForeignKey('Area', on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.nombre)


class Profesor(models.Model):
    """Profesores de cenecu"""

    nombre = models.CharField(max_length=16, blank=False)
    apellido = models.CharField(max_length=16, blank=False)
    titulo = models.CharField(max_length=20, blank=False)
    img_perfil = models.ImageField(upload_to='uploads/fotoProfesores/')
    frases_personal = models.CharField(max_length=100, blank=False)
    biografia = models.CharField(max_length=255, blank=False)
    area_especializacion = models.ForeignKey('Area', on_delete=models.CASCADE)
    url_linkedin = models.CharField(max_length=255, blank=False)
    curriculum = models.FileField(upload_to='uploads/pensums/')
    estado = models.CharField(max_length=10, blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.nombre)


class CursoProfesor(models.Model):
    """Relacion entre profesor y curso a dictar"""

    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)
    profesor_id = models.ForeignKey('Profesor', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.curso_id)


class Area(models.Model):
    """Areas de interes de cenecu"""

    nombre = models.CharField(max_length=25, blank=False)
    descripcion = models.CharField(max_length=100)
    img_area = models.ImageField(upload_to='uploads/areas/')
    estado = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return "{}".format(self.nombre)


class Anuncio(models.Model):
    """Anuncios y promociones de cenecu"""

    descripcion = models.CharField(max_length=255, blank=False)
    img_anuncio = models.ImageField(upload_to='uploads/anuncio/')
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=10, blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "anuncio: " + self.descripcion


class Frase(models.Model):
    """Frases motivacionales de cenecuApp"""

    descripcion = models.CharField(max_length=100, blank=False)
    img_frase = models.ImageField(upload_to='uploads/frase/')
    estado = models.CharField(max_length=10, blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.descripcion)


class GoalsList(models.Model):
    """GoalList"""

    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.curso_id)


class AreaInteres(models.Model):
    """Areas de Interes de los usuarios"""

    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    area_id = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.area_id)


class UsuarioRol(models.Model):
    """Roles de los usuarios"""

    roles = (('cliente', 'cliente'), ('admin', 'administrador'),
             ('bloqueado', 'UsuarioBloqueado'))
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, blank=False, choices=roles)

    def __str__(self):
        return "{}".format(self.usuario_id)


class Nota(models.Model):
    """Notas de los usuarios"""

    titulo = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255)
    fecha_limite = models.DateField()
    notificacion = models.BooleanField()
    fecha_notificacion = models.DateTimeField()
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.titulo)


class ContenidoCompartido(models.Model):
    """Contenido compartido por las redes sociales"""

    rsocial = (('tw', 'Twitter'), ('wa', 'Whatsapp'), ('fb', 'Facebook'))
    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compartido = models.DateTimeField(auto_now_add=True)
    red_social = models.CharField(max_length=2, blank=False, choices=rsocial)

    def __str__(self):
        return "{}".format(self.red_social)


class RegistroUsuarioCurso(models.Model):
    """Solicitudes de registro a un curso"""

    curso_id = models.ForeignKey('Curso', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.curso_id)


class Telefonos(models.Model):
    """Telefonos de los usuarios"""

    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    telefonos = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return "{}".format(self.telefonos)
