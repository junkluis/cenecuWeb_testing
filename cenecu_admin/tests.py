""" tests.py """
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.contrib.auth.models import User

from django.urls import reverse

from django.test.client import RequestFactory
from django.test.client import Client
from django.test import TestCase


# Create your tests here.

class TestCalls(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #Test para Login en Cenecu Web
    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #Test para validar si el usuario no esta logeado, caso contrario se redirige al login
    def test_crear_cursos_not_logged(self):
        url = reverse('crear_curso')
        response = self.client.get(url)
        self.assertRedirects(response, '/login/')

    def test_crear_profesor_not_logged(self):
        url = reverse('crear_profesor')
        response = self.client.get(url)
        self.assertRedirects(response, '/login/')

    def test_crear_anuncio_not_logged(self):
        url = reverse('crear_anuncio')
        response = self.client.get(url)
        self.assertRedirects(response, '/login/')

    def test_crear_area_not_logged(self):
        url = reverse('crear_area')
        response = self.client.get(url)
        self.assertRedirects(response, '/login/')

    def test_crear_frase_not_logged(self):
        url = reverse('crear_frase')
        response = self.client.get(url)
        self.assertRedirects(response, '/login/')

    #Test para validar si el usuario esta logeado, caso contrario se redirige al login
    def test_crear_curso_logged(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('crear_curso'))
        self.assertTemplateUsed(response,'cenecu_admin/crear_curso.html','cenecu_admin/base.html')

    def test_crear_profesor_logged(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('crear_profesor'))
        self.assertTemplateUsed(response,'cenecu_admin/crear_profesor.html','cenecu_admin/base.html')
    
    def test_crear_anuncio_logged(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('crear_anuncio'))
        self.assertTemplateUsed(response,'cenecu_admin/crear_anuncio.html','cenecu_admin/base.html')
    
    def test_crear_area_logged(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('crear_area'))
        self.assertTemplateUsed(response,'cenecu_admin/crear_area.html','cenecu_admin/base.html')

    def test_crear_frase_logged(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('crear_frase'))
        self.assertTemplateUsed(response,'cenecu_admin/crear_frase.html','cenecu_admin/base.html')

    def test_nuevo_profesor(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('crear_profesor'))
        self.assertTemplateUsed(response,'cenecu_admin/crear_profesor.html','cenecu_admin/base.html')
        response2 = self.client.get(reverse('crear_profesor'))
        response2 = self.client.post('/nuevo_profesor',{'nombre':'Johan','apellido':'Canales', 'titulo':'Ingeniero','img_perfil':'/media/uploads/archivo.jpg',
            'frases_personal':'Hola','biografia':'Naci','area_especializacion':'Idiomas','url_linkedin':'www.linkedin.com'
            ,'curriculum':'media/files/cv.pdf','estado':'Activo'})
        self.assertEqual(response2.status_code, 404)


     


    