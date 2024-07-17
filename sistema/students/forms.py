from django import forms
from .models import Student

# Clase que hereda de forms.ModelForm para crear un formulario basado en el modelo Student.
class StudentForm(forms.ModelForm):   
    class Meta:
        model = Student # Especifica que el formulario se basa en el modelo Student
        fields = '__all__'  # Incluye todos los campos del modelo en el formulario