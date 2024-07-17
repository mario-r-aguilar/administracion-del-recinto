from django.urls import path
from . import views
# Importaciones para permitir renderizar imagenes desde sus rutas
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('addstudent/', views.addStudent, name='addstudent'),
    path('updatestudent/', views.updateStudent, name='updatestudent'),
    path('updatestudent/<int:dni>', views.updateStudent, name='updatestudent'),
    path('deleteStudent/<int:dni>', views.deleteStudent, name='deleteStudent' ),
    
    # Código para permitir renderizar imagenes desde sus rutas
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 