from django.shortcuts import render
from .models import Alumno, Escuela
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
    # select * from alumno
    # uso de ORM de Django
    listado = Escuela.objects.all()
    context = {"listado": listado}
    return render(resquest, 'listadoEscuela.html', context)