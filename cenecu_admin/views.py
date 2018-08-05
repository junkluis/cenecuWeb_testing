# -*- coding: utf-8 -*-
"""  views.py  """

from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from api.models import *
from django.utils.encoding import python_2_unicode_compatible
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import xlsxwriter
from io import BytesIO

def iniciar_sesion(request):
    """Inicia sesion en la app web del Administrador"""
    template = loader.get_template('cenecu_admin/page_login.html/')
	
    if(request.method == 'POST'):
        usuario = request.POST.get('usuario')
        clave = request.POST.get('password')
        user = authenticate(username = usuario, password = clave)
        if (user is not None):
            login(request, user)
            iduser = request.user.id
            usuario_rol = UsuarioRol.objects.get(usuario_id = iduser)
            if(usuario_rol.rol == "admin"  or usuario_rol.rol == "administrador"):
                messages.success(request, '¡Bienvenido!')
                return redirect('/')
            else:
                messages.success(request, 'Acceso no autotizado')
                return redirect ('/login')
        else:
        	messages.success(request, 'Usuario y/o contraseña no válidos')
        	return redirect ('/login')
    else:
    	notice = 'none'
	
    context = {
        'notice': notice 
    }
    return HttpResponse(template.render(context, request))
	

def cerrar_sesion (request):
    """Cierra sesion en la app web del Administrador"""	
    messages.success(request, 'Cierre de sesión exitoso')
    request.session.flush()
    logout(request)
    return redirect('/login')

	
def index(request):
    """Tras iniciar sesion, se muestra la pagina Detalle de Cursos"""
    if (request.user.is_authenticated):
        cursos = Curso.objects.all()
        context = {
            'cursos':cursos
        }
        return  render(request, "cenecu_admin/detalles_cursos.html", context)
    else:
        return redirect('/login')


def listar_profesores(request):
    """Lista los profesores de la base de datos"""
    if (request.user.is_authenticated):
        profesores = Profesor.objects.all()
        context = {
            'profesores':profesores
        }
        return  render(request, "cenecu_admin/detalles_profesores.html", context)
    else:
        return redirect('/login/')	


def listar_frases(request):
    """Lista las frases motivacionales de la base de datos"""
    if (request.user.is_authenticated):
        frases = Frase.objects.all()
        context = {
            'frases':frases
        }
        return  render(request, "cenecu_admin/detalles_frases.html", context)
    else:
        return redirect('/login/')


def listar_areas(request):
    """Lista las areas de interes de la base de datos"""
    if (request.user.is_authenticated):
        areas = Area.objects.all()
        context = {
            'areas':areas
        }
        return  render(request, "cenecu_admin/detalles_areas.html", context)
    else:
        return redirect('/login/')


def crear_area (request):
    """Muestra la pagina para crear una nueva area de interes"""
    if (request.user.is_authenticated):
        area = Area.objects.all()
        lista_area = Area.objects.all()
        print(lista_area)
        context = {
            'listaArea':lista_area
        }
        return  render(request, "cenecu_admin/crear_area.html", context)
    else:
        return redirect('/login/')	


def nueva_area(request):
    """Agrega una nueva area de interes a la base de datos """
    if (request.user.is_authenticated):
        context = {
        }
        if (request.POST):
            nueva_area = Area()
            nueva_area.nombre = request.POST.get('nombreArea')
            nueva_area.descripcion = request.POST.get('descripcion')
            nueva_area.img_area = request.FILES.get('img_area')
            nueva_area.estado = request.POST.get('estado')
            nueva_area.save()
            messages.success(request, '¡Área de Interés creada correctamente!')
        return redirect('/listarAreas/')
    else:
        return redirect('/login/')


def modificar_area(request):
    """Modifica una nueva area de interes a la base de datos """
    if (request.user.is_authenticated):
        if (request.POST):
            id_area = int(request.POST.get('idarea'))
            nueva_area = Area.objects.get(id = int(request.POST.get('idarea')))
            nueva_area.nombre = request.POST.get('nombreArea')
            nueva_area.descripcion = request.POST.get('descripcion')
            nueva_area.img_area = request.FILES.get('img_area')
            nueva_area.estado = request.POST.get('estado')
            nueva_area.save()
            messages.success(request, '¡Área de Interés modificada correctamente!')
        return redirect('/listarAreas/')
    else:
        return redirect('/login/')	

def editar_area(request, pk):
    """Muestra la pagina para editar un area de interes a la base de datos """
    if (request.user.is_authenticated):
        idarea = pk
        area_requerida = Area.objects.get(pk = pk)
        nombre = area_requerida.nombre
        descripcion = area_requerida.descripcion
        img_area = area_requerida.img_area
        estado = area_requerida.estado
        context = {
            'nombre': nombre,
            'descripcion': descripcion,
            'estado': estado,
            'imgarea': img_area,
            'idarea': idarea
        }
        return render(request, "cenecu_admin/editar_area.html", context)
    else:
        return redirect('/login/')


def eliminar_area(request, pk):
    """Elimina un area de interes de la base de datos"""
    if (request.user.is_authenticated):
        area = Area.objects.get(pk = pk)
        area.delete()
        messages.success(request, '¡Área de Interés eliminado correctamente!')
        return redirect('/listarAreas/')
    else:
        return redirect('/login/')


def crear_frase (request):
    """Muestra la pagina para crear una nueva frase"""
    if (request.user.is_authenticated):
        frase = Frase.objects.all()
        lista_frase = Frase.objects.all()
        print(lista_frase)
        context = {
            'listaFrase':lista_frase
        }
        return  render(request, "cenecu_admin/crear_frase.html", context)
    else:
        return redirect('/login/')	


def nueva_frase(request):
    """Agrega una nueva frase motivacional a la base de datos """
    if (request.user.is_authenticated):
        context = {
        }
        if (request.POST):
            nueva_frase = Frase()
            nueva_frase.descripcion = request.POST.get('descripcion')
            nueva_frase.img_frase = request.FILES.get('img_frase')
            nueva_frase.estado = request.POST.get('estado')
            nueva_frase.fecha_creado = datetime.datetime.now()
            nueva_frase.save()
            messages.success(request, '¡Frase motivacional creada correctamente!')
        return redirect('/listarFrases/')
    else:
        return redirect('/login/')

def modificar_frase(request):
    """Modifica una nueva frase motivacional a la base de datos """
    if (request.user.is_authenticated):
        if (request.POST):
            id_frase = int(request.POST.get('idfrase'))
            nueva_frase = Frase.objects.get(id = int(request.POST.get('idfrase')))
            nueva_frase.descripcion = request.POST.get('descripcion')
            nueva_frase.img_frase = request.FILES.get('img_frase')
            nueva_frase.estado = request.POST.get('estado')
            nueva_frase.fecha_creado = datetime.datetime.now()
            nueva_frase.save()
            messages.success(request, '¡Frase motivacional modificada correctamente!')
        return redirect('/listarFrases/')
    else:
        return redirect('/login/')	

def editar_frase(request, pk):
    """Muestra la pagina para editar una frase motivacional"""
    if (request.user.is_authenticated):
        idfrase = pk
        frase_requerida = Frase.objects.get(pk = pk)
        descripcion = frase_requerida.descripcion
        img_frase = frase_requerida.img_frase
        estado = frase_requerida.estado
        context = {
            'descripcion': descripcion,
            'estado': estado,
            'imgFrase': img_frase,
            'idfrase': idfrase
        }
        return render(request, "cenecu_admin/editar_frase.html", context)
    else:
        return redirect('/login/')	


def eliminar_frase(request, pk):
    """Elimina a frase motivacional de la base de datos"""
    if (request.user.is_authenticated):
        frase = Frase.objects.get(pk = pk)
        frase.delete()
        messages.success(request, '¡Frase eliminada correctamente!')
        return redirect('/listarFrases/')
    else:
        return redirect('/login/')	


def crear_curso (request):
    """Muestra la pagina para crear un nuevo curso"""
    if (request.user.is_authenticated):
        area = Area.objects.all()
        lista_profesor = Profesor.objects.all()
        print(lista_profesor)
        context = {
            'area':area,
            'listaProfesor':lista_profesor
        }
        return  render(request, "cenecu_admin/crear_curso.html", context)
    else:
        return redirect('/login/')	


def nuevo_curso(request):
    """Agrega un nuevo curso a la base de datos, 
        crea relacion entre profesor y curso """
    if (request.user.is_authenticated):
        context = {
        }
        if (request.POST):
            nuevo_curso = Curso()
            nuevo_curso.nombre = request.POST.get('nombreCurso')
            nuevo_curso.descripcion = request.POST.get('descripcion')
            nuevo_curso.pensum = request.FILES.get('pensum')
            nuevo_curso.duracion_cant = request.POST.get('duracion')
            nuevo_curso.duracion_tipo = request.POST.get('tipoDuracion')
            nuevo_curso.costo = request.POST.get('costo')
            nuevo_curso.img_curso = request.FILES.get('imagen')
            area_requerido = Area.objects.get(pk=request.POST.get('area'))
            nuevo_curso.area_estudio = area_requerido
            nuevo_curso.estado = "Activo"
            nuevo_curso.fecha_creado = datetime.datetime.now()
            nuevo_curso.save()
            curso_profesor = CursoProfesor()
            curso_profesor.curso_id = nuevo_curso
            curso_profesor.profesor_id = Profesor.objects.get(pk = request.POST.get('profesor'))
            curso_profesor.save()
            messages.success(request, '¡Curso creado correctamente!')
        return redirect('/')
    else:
        return redirect('/login/')	


def modificar_curso(request):
    """Edita un curso que se encuentra en la base de datos"""
    if (request.user.is_authenticated):
        if (request.POST):
            id_curso = int(request.POST.get('idcurso'))
            nue_curso = Curso.objects.get(id = int(request.POST.get('idcurso')))
            nue_curso.nombre = request.POST.get('nombreCurso')
            nue_curso.descripcion = request.POST.get('descripcion')
            nue_curso.pensum = request.FILES.get('pensum')
            nue_curso.duracion_cant = request.POST.get('duracion')
            nue_curso.costo = request.POST.get('costo')
            nue_curso.img_curso = request.FILES.get('imgCurso')
            nue_curso.estado = "Activo"
            nue_curso.fecha_creado = datetime.datetime.now()
            nue_curso.save()
            messages.success(request, '¡Curso modificado correctamente!')
        return redirect ('/')
    else:
        return redirect('/login/')	


def editar_curso(request, pk):
    """Muestra la pagina para editar un curso"""
    if (request.user.is_authenticated):
        idcurso = pk
        lista_profesores = Profesor.objects.all()
        lista_area = Area.objects.all()
        curso_requerido = Curso.objects.get(pk = pk)
        curso_profesor = CursoProfesor.objects.get(curso_id = curso_requerido.pk)
        nombre_profesor = curso_profesor.profesor_id
        nombre = curso_requerido.nombre
        descripcion = curso_requerido.descripcion
        url_pensum = curso_requerido.pensum
        duracion = curso_requerido.duracion_cant
        duracion_tipo = curso_requerido.duracion_tipo
        costo = curso_requerido.costo
        img_curso = curso_requerido.img_curso
        estado = curso_requerido.estado
        area_requerido = Area.objects.get(pk = curso_requerido.area_estudio.pk)
        area_estudio = area_requerido
        context = {
            'nombre':nombre,
            'descripcion': descripcion,
            'duracion': duracion,
            'duracion_tipo': duracion_tipo,
            'costo': costo,
            'lista_profesores': lista_profesores,
            'estado': estado,
            'imgCurso': img_curso,
            'urlPensum': url_pensum,
            'area_estudio':area_estudio,
            'listaArea':lista_area,
            'nombreProfesor': nombre_profesor,
            'idcurso': idcurso
        }
        return render(request, "cenecu_admin/editar_curso.html", context)
    else:
        return redirect('/login/')	



def eliminar_curso(request, pk):
    """Elimina un curso de la base de datos"""
    if (request.user.is_authenticated):
        curso = Curso.objects.get(pk = pk)
        curso.estado = "Inactivo"
        curso.save()
        messages.success(request, '¡Curso eliminado correctamente!')
        return redirect('/')
    else:
        return redirect('/login/')  


def crear_profesor (request):
    """Muestra la pagina para crear un nuevo perfil de profesor"""
    if (request.user.is_authenticated):
        areas = Area.objects.all()
        context = {
            'areas': areas,
        }
        return  render(request, "cenecu_admin/crear_profesor.html", context)
    else:
        return redirect('/login/')


def nuevo_profesor(request):
    """Agrega un nuevo perfil de profesor a la base de datos"""
    if (request.user.is_authenticated):
        if (request.POST):
            nuevo_profesor = Profesor()
            nuevo_profesor.nombre = request.POST.get('nombreProfesor')
            nuevo_profesor.apellido = request.POST.get('apellidoProfesor')
            nuevo_profesor.titulo = request.POST.get('titulo')
            nuevo_profesor.img_perfil = request.FILES.get('img_perfil')
            nuevo_profesor.frases_personal = request.POST.get('frases_personal')
            nuevo_profesor.biografia = request.POST.get('biografia')
            area_id = request.POST.get('area_especializacion')
            area_select = Area.objects.get(pk = area_id)
            nuevo_profesor.area_especializacion = area_select
            nuevo_profesor.url_linkedin = request.POST.get('url_linkedin')
            nuevo_profesor.curriculum = request.FILES.get('curriculum')
            nuevo_profesor.estado = request.POST.get('estado')
            nuevo_profesor.save()
            messages.success(request, '¡Profesor creado correctamente!')
        return redirect('/listarProfesores/')
    else:
        return redirect('/login/')	


def modificar_profesor(request):
    """Edita un perfil de profesor que se encuentra en la base de datos"""
    if (request.user.is_authenticated):
        if (request.POST):
            idprofesor = int(request.POST.get('idprofesor'))
            nuevo_profesor = Profesor.objects.get(id = int(request.POST.get('idprofesor')))
            nuevo_profesor.nombre = request.POST.get('nombreProfesor')
            nuevo_profesor.apellido = request.POST.get('apellidoProfesor')
            nuevo_profesor.titulo = request.POST.get('titulo')
            nuevo_profesor.img_perfil = request.FILES.get('img_perfil')
            nuevo_profesor.frases_personal = request.POST.get('frases_personal')
            nuevo_profesor.biografia = request.POST.get('biografia')
            nuevo_profesor.url_linkedin = request.POST.get('url_linkedin')
            nuevo_profesor.curriculum = request.FILES.get('curriculum')
            nuevo_profesor.estado = request.POST.get('estado')
            nuevo_profesor.save()
            messages.success(request, '¡Profesor modificado correctamente!')
        return redirect ('/listarProfesores/')
    else:
        return redirect('/login/')


def editar_profesor(request, pk):
    """Muestra la pagina para editar un perfil de profesor"""
    if (request.user.is_authenticated):
        idprofesor = pk
        lista_areas = Area.objects.all()
        profesor_requerido = Profesor.objects.get(pk = pk)
        nombre = profesor_requerido.nombre
        apellido = profesor_requerido.apellido
        titulo = profesor_requerido.titulo
        img_perfil = profesor_requerido.img_perfil
        frases_personal = profesor_requerido.frases_personal
        biografia = profesor_requerido.biografia
        url_linkedin = profesor_requerido.url_linkedin
        curriculum = profesor_requerido.curriculum
        estado = profesor_requerido.estado
        area_requerido = Area.objects.get(pk = profesor_requerido.area_especializacion.pk)
        area_especializacion = area_requerido
        context = {
            'nombre':nombre,
            'apellido': apellido,
            'titulo': titulo,
            'img_perfil': img_perfil,
            'frases_personal': frases_personal,
            'biografia': biografia,
            'url_linkedin': url_linkedin,
            'curriculum': curriculum,
            'areas': lista_areas,
            'area_especializacion': area_especializacion,
            'estado': estado,
            'idprofesor': idprofesor
        }
        return render(request, "cenecu_admin/editar_profesor.html", context)
    else:
        return redirect('/login/')


def eliminar_profesor(request, pk):
    """Elimina un perfil de profesor de la base de datos"""
    if (request.user.is_authenticated):
        profesor = Profesor.objects.get(pk = pk)
        profesor.delete()
        messages.success(request, '¡Profesor eliminado correctamente!')
        return redirect('/listarProfesores/')
    else:
        return redirect('/login/')


def listar_anuncios(request):
    """Lista los anuncios de la base de datos"""
    if (request.user.is_authenticated):
        anuncios = Anuncio.objects.all()
        context = {
            'anuncios':anuncios
        }
        return  render(request, "cenecu_admin/detalles_anuncios.html", context)
    else:
        return redirect('/login/')


def crear_anuncio(request):
    """Muestra la pagina para crear una nueva publicidad"""
    if (request.user.is_authenticated):
        anuncio = Anuncio.objects.all()
        lista_anuncio = Anuncio.objects.all()
        print(lista_anuncio)
        context = {
            'listaAnuncio':lista_anuncio
        }
        return  render(request, "cenecu_admin/crear_anuncio.html", context)
    else:
        return redirect('/login/')  


def nuevo_anuncio(request):
    """Agrega un nuevo anuncio a la base de datos """
    if (request.user.is_authenticated):
        context = {
        }
        if (request.POST):
            nuevo_anuncio = Anuncio()
            nuevo_anuncio.descripcion = request.POST.get('descripcion')
            nuevo_anuncio.img_anuncio = request.FILES.get('img_anuncio')
            nuevo_anuncio.estado = request.POST.get('estado')
            nuevo_anuncio.fecha_limite = request.POST.get('fecha_limite')
            nuevo_anuncio.fecha_creado = datetime.datetime.now()
            nuevo_anuncio.save()
            messages.success(request, '¡Anuncio publicitario creado correctamente!')
        return redirect('/listarAnuncios/')
    else:
        return redirect('/login/')

def modificar_anuncio(request):
    """Modifica un nuevo anuncio a la base de datos """
    if (request.user.is_authenticated):
        if (request.POST):
            id_anuncio = int(request.POST.get('idanuncio'))
            nueva_anuncio = Anuncio.objects.get(id = int(request.POST.get('idanuncio')))
            nueva_anuncio.descripcion = request.POST.get('descripcion')
            nueva_anuncio.img_anuncio = request.FILES.get('img_anuncio')
            nueva_anuncio.estado = request.POST.get('estado')
            nueva_anuncio.fecha_limite = request.POST.get('fecha_limite')
            nueva_anuncio.fecha_creado = datetime.datetime.now()
            nueva_anuncio.save()
            messages.success(request, '¡Anuncio publicitario modificado correctamente!')
        return redirect('/listarAnuncios/')
    else:
        return redirect('/login/')  

def editar_anuncio(request, pk):
    """Muestra la pagina para editar una frase motivacional"""
    if (request.user.is_authenticated):
        idanuncio = pk
        anuncio_requerida = Anuncio.objects.get(pk = pk)
        descripcion = anuncio_requerida.descripcion
        img_anuncio = anuncio_requerida.img_anuncio
        fecha_limite = anuncio_requerida.fecha_limite
        estado = anuncio_requerida.estado
        context = {
            'descripcion': descripcion,
            'estado': estado,
            'img_anuncio': img_anuncio,
            'fecha_limite': fecha_limite,
            'idanuncio': idanuncio
        }
        return render(request, "cenecu_admin/editar_anuncio.html", context)
    else:
        return redirect('/login/')  


def eliminar_anuncio(request, pk):
    """Elimina a frase motivacional de la base de datos"""
    if (request.user.is_authenticated):
        anuncio = Anuncio.objects.get(pk = pk)
        anuncio.delete()
        messages.success(request, '¡Anuncio publicitario eliminado correctamente!')
        return redirect('/listarAnuncios/')
    else:
        return redirect('/login/')  


def visualizar_reporte (request):
    if (request.user.is_authenticated):
        context ={

        }
        return render(request, "cenecu_admin/reportes.html", context)
    else:
        return redirect('/login/')


def visualizar_reporte (request):
    """Genera mapas para visualizar graficos """
    if (request.user.is_authenticated):
        """Genera mapa para visualizar numero de usuarios por area de interes """
        lista_area = list(Area.objects.all())
        lista_curso = list(Curso.objects.all())
        numeroareas=len((lista_area))
        dict_curso_numerointeres = {}
        while (numeroareas !=0):
            idarea = lista_area[numeroareas-1].id
            nombreArea = (Area.objects.get(pk = idarea).nombre)
            dict_curso_numerointeres[nombreArea] = AreaInteres.objects.filter(area_id=idarea).count()
            numeroareas = numeroareas -1
        listaUsuarioCurso = list(RegistroUsuarioCurso.objects.all())
        numeroCursos = len(lista_curso)
        dict_curso_numregistro = {}
        while (numeroCursos !=0):
            idcurso=lista_curso[numeroCursos-1].id
            nombre_curso = (Curso.objects.get(pk= idcurso).nombre)
            dict_curso_numregistro[nombre_curso] = RegistroUsuarioCurso.objects.filter(curso_id=idcurso).count()
            numeroCursos = numeroCursos -1
        dict_curso_red_compartida = {}
        total_cursos = len(lista_curso)
        while (total_cursos !=0):
            dict_red_numerocompartido = {}
            lista_red_numerocompartido = []
            id_curso = lista_curso[total_cursos-1].id
            nombre_curss = (Curso.objects.get(pk= id_curso).nombre)
            num_comp_tw  = ContenidoCompartido.objects.filter(curso_id=id_curso).filter(red_social='tw').count()
            num_comp_fb = ContenidoCompartido.objects.filter(curso_id=id_curso).filter(red_social='fb').count()
            num_comp_wa = ContenidoCompartido.objects.filter(curso_id=id_curso).filter(red_social='wa').count()
            lista_red_numerocompartido = [num_comp_tw,num_comp_fb,num_comp_wa]
            dict_curso_red_compartida[nombre_curss] = lista_red_numerocompartido
            total_cursos = total_cursos -1
        print(dict_curso_red_compartida)
        context = {
             'dict_curso_numerointeres' : dict_curso_numerointeres,
             'dict_curso_numregistro' : dict_curso_numregistro,
             'dict_curso_red_compartida': dict_curso_red_compartida,
             'lista_curso': lista_curso
        }
        return render(request, "cenecu_admin/reportes.html", context)
    else:
        return redirect('/login/')

def reporte_user_area_interes(request):
    if(request.user.is_authenticated):
        lista_area = list(Area.objects.all())
        lista_curso = list(Curso.objects.all())
        numeroareas=len((lista_area))
        dict_curso_numerointeres = {}
        while (numeroareas !=0):
            idarea = lista_area[numeroareas-1].id
            nombreArea = (Area.objects.get(pk = idarea).nombre)
            dict_curso_numerointeres[nombreArea] = AreaInteres.objects.filter(area_id=idarea).count()
            numeroareas = numeroareas -1
        context = {
            'dict_curso_numerointeres' : dict_curso_numerointeres,
        }
        return render(request, "cenecu_admin/reporte_usuario_area.html", context)
    else:
        return redirect('/login/')

def reporte_user_solicitud_registro(request):
    if(request.user.is_authenticated):
        lista_curso = list(Curso.objects.all())
        numeroCursos = len(lista_curso)
        dict_curso_numregistro = {}
        while (numeroCursos !=0):
            idcurso=lista_curso[numeroCursos-1].id
            nombre_curso = (Curso.objects.get(pk= idcurso).nombre)
            if( RegistroUsuarioCurso.objects.filter(curso_id=idcurso).count() > 0):
                dict_curso_numregistro[nombre_curso] = RegistroUsuarioCurso.objects.filter(curso_id=idcurso).count()
            numeroCursos = numeroCursos -1
        print(dict_curso_numregistro)
        total_cursos = len(dict_curso_numregistro)
        print(len(dict_curso_numregistro))
        context ={
            'dict_curso_numregistro': dict_curso_numregistro,
            'total_cursos': total_cursos,
        }
        return render(request, "cenecu_admin/reporte_usuario_solicitud.html", context)
    else:
        return redirect('/login/')






def exportar_repo(request):
    if (request.user.is_authenticated):


        tipo = request.GET.get('tipoRepo')
        
        reporte = xlsxwriter.Workbook("media/reportes/reporte_cenecu.xlsx")
        reporte.title = "test"
        worksheet = reporte.add_worksheet()
        worksheet.write('A1', 'Reporte: Cantidad de Usuarios por Áreas de Interés')
        chart = reporte.add_chart({'type': 'column'})
        data = [
                [1, 2, 3, 4, 5],
                [2, 4, 6, 8, 10],
                [3, 6, 9, 12, 15],
            ]

        worksheet.write_column('A2', data[0])
        worksheet.write_column('B2', data[1])
        worksheet.write_column('C2', data[2])

        chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
        chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
        chart.add_series({'values': '=Sheet1!$C$1:$C$5'})
        worksheet.insert_chart('A7', chart)
        reporte.close()

        data = {'ok': 'ok' }
        return JsonResponse(data)
    else:
        return redirect('/login/')

def ajaxReporteCompartido(request):
    lista_area = list(Area.objects.all())
    lista_area_interes = list(AreaInteres.objects.all())
    listaUsuarioCurso = list(RegistroUsuarioCurso.objects.all())
    numeroareas=len((lista_area))
    lista_reporte = []
    while (numeroareas !=0):
        dict_curso_numerointeres = {}
        idarea = lista_area[numeroareas-1].id
        nombreArea = Area.objects.get(pk = idarea).nombre
        dict_curso_numerointeres[nombreArea] = AreaInteres.objects.filter(area_id=idarea).count()
        numeroareas = numeroareas -1
        lista_reporte.append(dict_curso_numerointere)
    context = {
         'lista_reporte' : lista_reporte,
    }

    return redmder(context)