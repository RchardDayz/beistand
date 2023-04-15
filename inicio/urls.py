
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.crear_contacto, name= 'contacto'),
    path('contacto/lista-contactos/', views.lista_contactos),
    path('contacto/<int:id>/eliminar/', views.eliminar_contacto),
    path('contacto/<int:id>/modificar/', views.modificar_contacto),
           
]
