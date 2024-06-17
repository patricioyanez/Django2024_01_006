from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='index'),
    path('index', views.index, name='index'),
    path('listadoEstudiante', views.listadoEstudiante, name='listadoEstudiante'),
    path('listadoEscuela', views.listadoEscuela, name='listadoEscuela'),
    path('listadoCarrera', views.listadoCarrera, name='listadoCarrera'),
    path('ingresarEscuela', views.ingresarEscuela, name='ingresarEscuela'),
    path('ingresarCarrera', views.ingresarCarrera, name='ingresarCarrera'),
    path('eliminarEscuela/<str:pk>', views.eliminarEscuela, name='eliminarEscuela'),
    path('eliminarCarrera/<str:pk>', views.eliminarCarrera, name='eliminarCarrera'),
    path('eliminarUsuario/<str:pk>', views.eliminarUsuario, name='eliminarUsuario'),
    path('guardarEscuela', views.guardarEscuela, name='guardarEscuela'),
    path('guardarUsuario', views.guardarUsuario, name='guardarUsuario'),
    path('buscarEscuela/<str:pk>', views.buscarEscuela, name='buscarEscuela'),
    path('buscarUsuario/<str:pk>', views.buscarUsuario, name='buscarUsuario'),
]

# Ejercicio: realizar guardar para carrera y alumno
# agregar link en el menu para ingresar a usuario
# permitir listar los usuarios al presionar el boton listar en form usuario