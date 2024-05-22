from django.contrib import admin
from .models import Escuela

# Register your models here.
admin.site.register(Escuela)

# revisar los tipos de datos validos para models.
# agregar crud para carrera y alumno