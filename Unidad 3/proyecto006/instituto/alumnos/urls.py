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
]

# Tarea: Para alumno: agregar link en listado y crear el ingresar