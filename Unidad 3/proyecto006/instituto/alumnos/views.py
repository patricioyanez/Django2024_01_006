from django.shortcuts import render
from .models import Alumno, Escuela, Carrera
# Create your views here.

def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):
    context = {}
    return render(request, 'index.html', context)


def listadoEstudiante(resquest):
    # select * from alumno
    # uso de ORM de Django
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(resquest, 'listadoEstudiante.html', context)

def listadoEscuela(resquest):
    listado = Escuela.objects.all()
    context = {"listado": listado}
    return render(resquest, 'listadoEscuela.html', context)

def listadoCarrera(resquest):
    listado = Carrera.objects.all()
    context = {"listado": listado}
    return render(resquest, 'listadoCarrera.html', context)

def ingresarEscuela(request):    
    context = {}
    return render(request, 'ingresarEscuela.html', context)

def ingresarCarrera(request):    
    escuelas = Escuela.objects.all()
    context = {"escuelas": escuelas}
    return render(request, 'ingresarCarrera.html', context)