from django.contrib import admin
from .models import Student

# Register your models here.
# Registra el modelo Student en el panel de administrador de Django, para gestionar los objetos Student a través de su interfaz
admin.site.register(Student)