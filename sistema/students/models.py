from typing import Any
from django.db import models

# Create your models here.
class Student(models.Model):
    dni = models.IntegerField(primary_key=True, verbose_name='DNI')
    studentName = models.CharField(max_length=100, verbose_name='Nombre Completo')
    category = models.CharField(max_length=100, verbose_name='Categoría')
    email= models.EmailField(verbose_name='Correo')
    phone = models.IntegerField(verbose_name='Teléfono')
    responsible = models.CharField(max_length=100,null=True, verbose_name='Responsable')
    startDate = models.DateField(verbose_name='Fecha de Inicio')
    orienteer = models.CharField(max_length=100, verbose_name='Orientador')
    medicalFile = models.CharField(max_length=100, verbose_name='Ficha Médica')
    dniImage = models.ImageField(upload_to='images/',null=True, verbose_name='Foto del DNI')
    status = models.CharField(max_length=100, verbose_name='Estado')
    comments = models.TextField(null=True, verbose_name='Comentarios')
    actionPlan = models.TextField(null=True, verbose_name='Plan de Acción')
    
    def __str__(self):
        return self.studentName
    
    # Borra fisicamente la imagen
    def delete(self, using=None, keep_parents=False):
        self.dniImage.storage.delete(self.dniImage.name)
        super().delete()