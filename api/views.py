# -*- coding: utf-8 -*-
"""Vistas de CRUD api"""



from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import Horario, Curso, Profesor, CursoProfesor, Area, Anuncio
from .models import Frase, GoalsList, AreaInteres, UsuarioRol, Nota
from .models import ContenidoCompartido, RegistroUsuarioCurso, Telefonos
from django.forms.models import model_to_dict
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


def api_index(request):
    '''
    function of views.py
    ''' 
    modelos = ['Horario', 'Curso', 'Profesor', 'CursoProfesor', 'Area',
               'Anuncio', 'Frase', 'GoalsList', 'AreaInteres', 'UsuarioRol',
               'Nota', 'ContenidoCompartido', 'RegistroUsuarioCurso',
               'Telefonos', 'loginCenecu', 'notasUser', 'borrarNota',
               'registrarUsuario', 'logOut', ]

    respuesta = {'modelos': modelos}
    return render(request, 'api/index.html', respuesta)


def error_404(request):
    '''
    function of views.py
    ''' 
    data = {}
    return render(request, 'api/error_404.html', data)


def error_500(request):
    '''
    function of views.py
    ''' 
    data = {}
    return render(request, 'api/error_500.html', data)


class HorarioView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

    def perform_create(self, serializer):
        '''
        function of views.py
        ''' 
        serializer.save()


class CursoView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def perform_create(self, serializer):
        '''
        function of views.py
        ''' 
        serializer.save()


class ProfesorView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def perform_create(self, serializer):
        '''
        function of views.py
        ''' 
        serializer.save()


class CursoProfesorView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = CursoProfesor.objects.all()
    serializer_class = CursoProfesorSerializer

    def perform_create(self, serializer):
        '''
        function of views.py
        ''' 
        serializer.save()


class AreaView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def perform_create(self, serializer):
        '''
        function of views.py
        ''' 
        serializer.save()


class AnuncioView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def perform_create(self, serializer):
        '''
        función de AnuncioView
        ''' 
        serializer.save()


class FraseView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer

    def perform_create(self, serializer):
        '''
        función de FraseView
        ''' 
        serializer.save()


class GoalsListView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = GoalsList.objects.all()
    serializer_class = GoalsListSerializer

    def perform_create(self, serializer):
        '''
        función de GoalListView
        ''' 
        serializer.save()


class AreaInteresView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = AreaInteres.objects.all()
    serializer_class = AreaInteresSerializer

    def perform_create(self, serializer):
        '''
        función de AreaInteresesView
        '''         
        serializer.save()


class UsuarioRolView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer

    def perform_create(self, serializer):
        '''
        función de UsuarioRolView
        ''' 
        serializer.save()


class NotaView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    def perform_create(self, serializer):
        '''
        función de NotaView
        '''         
        serializer.save()


class ContenidoCompartidoView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = ContenidoCompartido.objects.all()
    serializer_class = ContenidoCompartidoSerializer

    def perform_create(self, serializer):
        '''
        función de ContenidoCompartidoView
        ''' 
        serializer.save()


class RegistroUsuarioCursoView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = RegistroUsuarioCurso.objects.all()
    serializer_class = RegistroUsuarioCursoSerializer

    def perform_create(self, serializer):
        '''
        función de RegistroUsuarioCursoView
        '''         
        serializer.save()


class TelefonosView(generics.ListCreateAPIView):
    '''
    class of views.py
    ''' 
    queryset = Telefonos.objects.all()
    serializer_class = TelefonosSerializer

    def perform_create(self, serializer):
        '''
        función de TelefonosView
        '''         
        serializer.save()


class HorarioEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class CursoEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ProfesorEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


class CursoProfesorEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = CursoProfesor.objects.all()
    serializer_class = CursoProfesorSerializer


class AreaEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AnuncioEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


class FraseEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer


class GoalsListEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = GoalsList.objects.all()
    serializer_class = GoalsListSerializer


class AreaInteresEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = AreaInteres.objects.all()
    serializer_class = AreaInteresSerializer


class UsuarioRolEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer


class NotaEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


class ContenidoCompartidoEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = ContenidoCompartido.objects.all()
    serializer_class = ContenidoCompartidoSerializer


class RegistroUsuarioCursoEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = RegistroUsuarioCurso.objects.all()
    serializer_class = RegistroUsuarioCursoSerializer


class TelefonosEdit(generics.RetrieveUpdateDestroyAPIView):
    '''
    class of views.py
    ''' 
    queryset = Telefonos.objects.all()
    serializer_class = TelefonosSerializer


@api_view(['GET', 'POST'])
def hello_world(request):
    '''
    función hello_worlf
    ''' 
    if request.method == 'POST':
        username = 'testUser'
        password = 'Password123'
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return Response({"user": user.username})
        else:
            return Response({"user": "you are not my dad"})
    else:
        return Response({"message": "Hello, world!"})


# login API
@api_view(['GET', 'POST'])
def login_cenecu(request):
    '''
    function of views.py
    ''' 
    context = {}

    if request.method == 'POST':
        print(request.data)
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            user_rol = UsuarioRol.objects.get(usuario_id = user.pk)
            context = {
                'user': model_to_dict(user),
                'rol': user_rol.rol,
                'err': None
            }
            return Response(context)
        else:
            return Response({"err": "falloLogin"})
    else:
        return Response({"err": "permisosInvalidos"})


# Notas por usuario
@api_view(['GET'])
def notas_por_user(request, pk):
    '''
    function of views.py
    ''' 
    lista_notas = []
    notas_user = Nota.objects.all().filter(usuario_id = pk)
    for nota in notas_user:
        lista_notas.append(model_to_dict(nota))

    return Response(lista_notas)


@api_view(['GET'])
def borrar_nota(request, pk):
    '''
    function of views.py
    ''' 
    nota_borrar = Nota.objects.get(id = pk)
    if nota_borrar is not None:
        nota_borrar.delete()
        return Response({'msg': 'La nota se eliminó con exito'})
    else:
        return Response({'msg': 'err'})


@api_view(['POST'])
def registrar_usuario(request):
    '''
    function of views.py
    ''' 
    username = request.data["user"]
    password = request.data["pass"]
    apellido = request.data["apellido"]
    nombre = request.data["nombre"]
    email = request.data["email"]

    try:
        ext_user = User.objects.get(username = username)
    except User.DoesNotExist:
        ext_user = None

    if ext_user is None:
        if username != "" and password != "" and email != "":
            user = User.objects.create_user(username, email, password)
            if nombre != "":
                user.first_name = nombre
            if apellido != "":
                user.last_name = apellido
            user.save()
            return Response(model_to_dict(user))
        else:
            return Response({'msg': 'err'})
    else:
        return Response({'msg': 'extUser'})


@api_view(['GET'])
def log_out(request):
    '''
    function of views.py
    ''' 
    logout(request)
    return Response({'msg': 'logOut'})
