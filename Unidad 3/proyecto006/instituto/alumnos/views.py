from django.shortcuts import render
from .models import Alumno
# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def listadoEstudiante(resquest):
    # select * from alumno
    # uso de ORM de Django
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(resquest, 'index2.html', context)
