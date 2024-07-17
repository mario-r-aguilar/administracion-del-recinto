from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.

def index (request):
    # Guarda los datos creados a partir del modelo Student
    students = Student.objects.all() 
    # Envía los datos a la vista index
    return render(request,'index.html',{'students':students}) 

def addStudent (request):
    # Almacena los datos del formulario
    studentForm = StudentForm(request.POST or None, request.FILES or None) 
    # Verifica si el formulario es válido, guarda los datos en la BD y redirige al index
    if studentForm.is_valid():
        studentForm.save()
        return redirect('index')
    return render(request,'pages/add_students.html',{'studentForm': studentForm})

def updateStudent (request,dni):
    # Obtiene el estudiante mediante su DNI
    student = Student.objects.get(dni=dni)
    # Inicializa el formulario con los datos obtenidos
    studentForm = StudentForm(request.POST or None, request.FILES or None, instance=student)
    # Si los datos del formulario son válidos y se realizo un POST, guarda los datos en la BD y redirecciona al index
    if studentForm.is_valid() and request.POST:
        studentForm.save()
        return redirect('index')
    return render(request, 'pages/update_students.html',{'studentForm': studentForm})

def deleteStudent(request,dni):
    # Obtiene el estudiante mediante el DNI, lo borra y redirige al index
    student = Student.objects.get(dni=dni)
    student.delete()
    return redirect('index')