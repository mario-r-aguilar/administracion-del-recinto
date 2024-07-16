from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.

def index (request):
    students = Student.objects.all()
    return render(request,'index.html',{'students':students})

def addStudent (request):
    studentForm = StudentForm(request.POST or None, request.FILES or None)
    if studentForm.is_valid():
        studentForm.save()
        return redirect('index')
    return render(request,'pages/add_students.html',{'studentForm': studentForm})

def updateStudent (request,dni):
    student = Student.objects.get(dni=dni)
    studentForm = StudentForm(request.POST or None, request.FILES or None, instance=student)
    if studentForm.is_valid() and request.POST:
        studentForm.save()
        return redirect('index')
    return render(request, 'pages/update_students.html',{'studentForm': studentForm})

def deleteStudent(request,dni):
    student = Student.objects.get(dni=dni)
    student.delete()
    return redirect('index')