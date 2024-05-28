from django.contrib import admin
from .models import Escuela, Carrera, Alumno

# Register your models here.
admin.site.register(Escuela)
admin.site.register(Carrera)
admin.site.register(Alumno)

# TAREAS:
# revisar la documentación para ver otros tipos de datos para agregar a models
# agregar crud para carrera y alumno
# agregar 5 filas para cada modelos