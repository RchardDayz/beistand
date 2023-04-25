
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.crear_contacto, name= 'contacto'),
    path('contacto/lista-contactos/', views.lista_contactos, name='lista_contactos'),
    path('contacto/<int:id>/eliminar/', views.eliminar_contacto, name= 'eliminar_contacto'),
    path('contacto/<int:id>/modificar/', views.modificar_contacto, name='modificar_contacto'),
    
    path('contacto/<int:pk>/', views.MostrarContacto.as_view(), name='mostrar_contacto'),
    path('about/', views.about.as_view(), name= 'about'),
    path('servicios/', views.servicios.as_view(), name= 'servicios'),
    path('investigaciones2/', views.investigaciones.as_view(), name= 'investigaciones'),
    
    
    
           
]
