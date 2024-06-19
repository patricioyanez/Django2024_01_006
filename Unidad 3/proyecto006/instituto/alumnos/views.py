from django.shortcuts import render
from .models import Alumno, Escuela, Carrera, Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from instituto.settings import MEDIA_URL
# Create your views here.

@login_required
def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def listadoEstudiante(resquest):
    # select * from alumno
    # uso de ORM de Django
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(resquest, 'listadoEstudiante.html', context)
@login_required
def listadoEscuela(resquest):
    listado = Escuela.objects.all()
    context = {"listado": listado}
    return render(resquest, 'listadoEscuela.html', context)
@login_required
def listadoCarrera(resquest):
    listado = Carrera.objects.all()
    context = {"listado": listado}
    return render(resquest, 'listadoCarrera.html', context)
@login_required
def ingresarEscuela(request):    
    context = {}
    return render(request, 'ingresarEscuela.html', context)
@login_required
def ingresarCarrera(request):    
    escuelas = Escuela.objects.all()
    context = {"escuelas": escuelas}
    return render(request, 'ingresarCarrera.html', context)
@login_required
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
@login_required
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
@login_required
def eliminarUsuario(request,pk):
    context = {}
    try:
        item = Usuario.objects.get(pk = pk)
        item.delete()
        context['exito'] = 'El registro fue eliminado'
    except:
        context['error'] = 'Error al eliminar el registro'

    context['listado'] = Usuario.objects.all()
    context['form'] = UsuarioForm()
    return render(request, 'ingresarUsuarioForm.html', context)
@login_required
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
@login_required
def guardarUsuario(request):
    context = {'form': UsuarioForm()}
    # captura de solicitud realizada por el usuario
    if request.method == 'POST':
        # detecta si el boton guardar fue presionado
        if 'btnGuardar' in request.POST:
            item = None
            if request.POST['txtId'] != "0":
                item = Usuario.objects.get(pk=request.POST['txtId'])


            form = UsuarioForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                context['exito'] = "Los datos fueron guardados"
            else:
                print(form.errors)
                context['error'] = "Error al guardar los datos"
    context['listado'] = Usuario.objects.all()
    context['MEDIA_URL'] = MEDIA_URL
    return render(request, 'ingresarUsuarioForm.html', context)
@login_required
def buscarEscuela(request, pk):
    context = {}
    try:
        item = Escuela.objects.get(pk = pk)

        context['item'] = item
    except:
        context['error'] = 'Elemento seleccionado no encontrado'
    return render(request, 'ingresarEscuela.html', context)
@login_required
def buscarUsuario(request, pk):    
    context = {}
    try:
        item = Usuario.objects.get(pk = pk)
        context['form'] = UsuarioForm(instance=item)
        context['id'] = item.pk
    except:
        context['form'] = UsuarioForm()
        context['error'] = 'Elemento seleccionado no encontrado'

    context['listado'] = Usuario.objects.all()
    return render(request, 'ingresarUsuarioForm.html', context)