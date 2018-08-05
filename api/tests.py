# coding=utf-8
'''
pruebas sin terminar
faltan configurar los datos para cada prueba
'''

import os
from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.contrib.auth.models import User


'''
LISTA DE MODELOS

Horario
Curso
Profesor
CursoProfesor
Area
Anuncio
Frase
GoalsList
AreaInteres
UsuarioRol
Nota
ContenidoCompartido
RegistroUsuarioCurso
Telefonos

horario
curso
profesor
cursoProfesor
area
anuncio
frase
goalsList
areaInteres
usuarioRol
nota
contenidoCompartido
registroUsuarioCurso
telefonos
'''




areaTinfo = {'nombre': 'Idiomas', 'descripcion': 'Capacitaciones sobre ingles, francés, aleman', 
             'img_area': 'http://cenecu.pythonanywhere.com/media/uploads/areas/hello.jpg', 
             'estado': 'activo'}

cursoTinfo = {'nombre': 'Excel Avanzado',
              'descripcion': 'Lograr que al término del curso el participante conozca y maneje a cabalidad'+
                             ' cada una de las herramientas y funciones que se incluyen en el programa.',
              'pensum': 'http://cenecu.pythonanywhere.com/media/uploads/pensums/pensum_informatica.pdf',
              'duracion_cant': 55,
              'duracion_tipo': 'S',
              'costo': 170.0,
              'img_curso': 'http://cenecu.pythonanywhere.com/media/uploads/imagenes/Captura_de_pantalla_2018-07-12_a_las_08.41.46.png',
               'estado': 'Activo',
               'fecha_creado': '2018-07-12T13:43:18.200250Z'}

profesorTinfo = {"nombre": "Magaly Elizabeth",
                 "apellido": "Vélez Olaya",
                 "titulo": "Economista",
                 "img_perfil": "http://cenecu.pythonanywhere.com/media/uploads/fotoProfesores/Magaly_Velez.jpg",
                 "frases_personal": "La práctica afianza el conocimiento.",
                 "biografia": "Amplia experiencia en procesos administrativos, organización de oficinas",
                 "url_linkedin": "https://ec.linkedin.com/",
                 "curriculum": "http://cenecu.pythonanywhere.com/media/uploads/pensums/Curriculum_EC.MAGALY_VELEZ_ASIST.ADMINISTRATIVO.pdf",
                 "estado": "Activo",
                 "fecha_creado": "2018-07-23T19:24:09.064603Z"}




class HorarioTestCase(TestCase):

    def setUp(self):
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        self.client = APIClient()
        self.horarioData = {'curso_id' : cursoT.pk,
                            'dia' : 'L',
                            'hora_inicio' : '8',
                            'minutos_inicio' : '30',
                            'hora_fin' : '10',
                            'minutos_fin' : '30' }
        self.response = self.client.post(reverse('Horario'), self.horarioData, format='multipart')

    
    def test_crear_horario(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_horario(self):
        horario = Horario.objects.get()
        response = self.client.get(reverse('HorarioEdit', kwargs={'pk': horario.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, horario)

    def test_actualizar_un_horario(self):
        horario = Horario.objects.get()
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        nuevoHorario = {'curso_id' : cursoT.pk,
                        'dia' : 'M',
                        'hora_inicio' : '9',
                        'minutos_inicio' : '30',
                        'hora_fin' : '10',
                        'minutos_fin' : '30' }
        res = self.client.put(
            reverse('HorarioEdit', kwargs={'pk': horario.id}),
            nuevoHorario, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_borrar_un_horario(self):
        horario = Horario.objects.get()
        response = self.client.delete(
            reverse('HorarioEdit', kwargs={'pk': horario.id}),
                    format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)



class CursoProfesorTestCase(TestCase):
    
    def setUp(self):
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        profesorT = Profesor.objects.create(**profesorTinfo, area_especializacion=areaT)
        self.client = APIClient()
        self.cursoProfesorData = {'curso_id' : cursoT.pk,
                                  'profesor_id' : profesorT.pk }
        self.response = self.client.post(reverse('CursoProfesor'), self.cursoProfesorData, format='json')
    
    def test_crear_curso_profesor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_curso_profesor(self):
        cursoProfesor = CursoProfesor.objects.get()
        response = self.client.get(reverse('CursoProfesorEdit', kwargs={'pk': cursoProfesor.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_un_curso_profesor(self):
        areaT = Area.objects.create(**areaTinfo)
        otroCurso = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        profesorT = Profesor.objects.create(**profesorTinfo, area_especializacion=areaT)
        cursoProfesor = CursoProfesor.objects.get()
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        NuevoCursoProfesor = {'curso_id' : otroCurso.pk,
                             'profesor_id' : profesorT.pk }
        res = self.client.put(
            reverse('CursoProfesorEdit', kwargs={'pk': cursoProfesor.id}),
            NuevoCursoProfesor, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_borrar_un_curso_profesor(self):
        cursoProfesor = CursoProfesor.objects.get()
        response = self.client.delete(
            reverse('CursoProfesorEdit', kwargs={'pk': cursoProfesor.id}),
                    format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class GoalsListTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser2', 'myemail@test.com', 'password')
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        self.client = APIClient()
        self.goalsListData = { "usuario_id": usuarioT.pk,
                                   "curso_id": cursoT.pk,
                                   "estado": "activo" }
        self.response = self.client.post(reverse('GoalsList'), self.goalsListData, format='json')
    
    def test_crear_goals_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_goals_list(self):
        goals = GoalsList.objects.get()
        response = self.client.get(reverse('GoalsListEdit', kwargs={'pk': goals.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_un_goals_list(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        goals = GoalsList.objects.get()
        nuevoGoals = { "usuario_id": usuarioT.pk,
                       "curso_id": cursoT.pk,
                       "estado": "inactivo" }
        res = self.client.put(
            reverse('GoalsListEdit', kwargs={'pk': goals.id}),
            nuevoGoals, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_borrar_un_goals_list(self):
        goals = GoalsList.objects.get()
        response = self.client.delete(
            reverse('GoalsListEdit', kwargs={'pk': goals.id}),
                    format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class AreaInteresTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        areaT = Area.objects.create(**areaTinfo)
        self.client = APIClient()
        self.areaInteresData = { "usuario_id": usuarioT.pk,
                                   "area_id": areaT.pk }
        self.response = self.client.post(reverse('AreaInteres'), self.areaInteresData, format='json')
    
    def test_crear_area_interes(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class UsuarioRolTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        self.client = APIClient()
        self.usuarioRolData = { "usuario_id": usuarioT.pk,
                                   "rol": "cliente" }
        self.response = self.client.post(reverse('UsuarioRol'), self.usuarioRolData, format='json')
    
    def test_crear_usuario_rol(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class NotaTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        self.client = APIClient()
        self.usuarioData = { "titulo": "prueba",
                                "descripcion": "prueba",
                                "fecha_limite": "2018-07-22",
                                "notificacion": 'true',
                                "fecha_notificacion": "2018-07-22T23:15:00Z",
                                "usuario_id": usuarioT.pk,
                                "estado": "activo" }
        self.response = self.client.post(reverse('Nota'), self.usuarioData, format='json')
    
    def test_crear_nota(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class ContenidoCompartidoTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        self.client = APIClient()
        self.contenidoCompartidoData = { "curso_id": cursoT.pk,
                                         "usuario_id": usuarioT.pk,
                                         "fecha_compartido": "2018-07-28T02:28:43.958407Z",
                                         "red_social": "tw" }
        self.response = self.client.post(reverse('ContenidoCompartido'), self.contenidoCompartidoData, format='json')
    
    def test_crear_contenido_compartido(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class RegistroUsuarioCursoTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        self.client = APIClient()
        self.registroUsuarioCursoData = { "curso_id": cursoT.pk,
                                          "usuario_id": usuarioT.pk,
                                          "fecha_solicitud": "2018-07-28T02:28:43.958407Z" }
        self.response = self.client.post(reverse('RegistroUsuarioCurso'), self.registroUsuarioCursoData, format='json')
    
    def test_crear_registro_usuario_curso(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class TelefonosTestCase(TestCase):
    
    def setUp(self):
        usuarioT = User.objects.create_user('myuser', 'myemail@test.com', 'password')
        areaT = Area.objects.create(**areaTinfo)
        cursoT = Curso.objects.create(**cursoTinfo, area_estudio=areaT)
        self.client = APIClient()
        self.telefonoData = { "usuario_id": usuarioT.pk,
                              "telefonos": "123456789" }
        self.response = self.client.post(reverse('Telefonos'), self.telefonoData, format='json')
    
    def test_crear_telefono(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class UsuarioTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.userData = { "user": "prueba",
                              "pass": "contrasenia",
                              "apellido": "John",
                              "nombre": "Snow",
                              "email": "john@gmail.com" }
        self.response = self.client.post(reverse('registrar_usuario'), self.userData, format='json')
    
    def test_registrar_usuario(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

