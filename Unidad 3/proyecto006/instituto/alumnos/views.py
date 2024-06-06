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

def eliminarEscuela(request,pk):
    context = {}
    try:
        item = Escuela.objects.get(pk = pk)
        item.delete()
        context['exito'] = 'El registro fue eliminado'
    except:
        context['error'] = 'Error al eliminar el registro'
    
    listado = Escuela.objects.all()
    context['listado'] = listado
    return render(request, 'listadoEscuela.html', context)

def eliminarCarrera(request,pk):
    context = {}
    try:
        item = Carrera.objects.get(pk = pk)
        item.delete()
        context['exito'] = 'El registro fue eliminado'
    except:
        context['error'] = 'Error al eliminar el registro'
    
    listado = Carrera.objects.all()
    context['listado'] = listado
    return render(request, 'listadoCarrera.html', context)

def guardarEscuela(request):
    context = {}
    # captura de solicitud realizada por el usuario
    if request.method == 'POST':
        # captura de datos del form a variables
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        # detecta si el boton guardar fue presionado
        if 'btnGuardar' in request.POST:
            # validar!!!
            if len(nombre.strip()) < 1:
                context['error'] = "No especifico el nombre de la escuela"
            else:
                if id == "0":
                    Escuela.objects.create(nombre=nombre, activo=activo)
                else:
                    # 1ra forma: buscar item a modificar. puede causar excepción si no existe
                    # item = Escuela.objects.get(pk = id)
                    
                    # 2da forma: crear un objeto, completar los atributos y save.
                    # Puede causar un nuevo ingreso de datos si el id no coincide con alguno
                    # registrado en la tabla
                    item = Escuela() 
                    item.nombre = nombre
                    item.activo = activo
                    item.id = id
                    item.save()
                
                context['exito'] = "Los datos fueron guardados"

    return render(request, 'ingresarEscuela.html', context)

def buscarEscuela(request, pk):
    context = {}
    try:
        item = Escuela.objects.get(pk = pk)

        context['item'] = item
    except:
        context['error'] = 'Elemento seleccionado no encontrado'
    return render(request, 'ingresarEscuela.html', context)