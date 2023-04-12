
from django.urls import path
from inicio import views

# app_name = 'inicio'

urlpatterns = [
    path('', views.inicio),
    path('contacto/', views.crear_contacto),
    path('lista-contactos/', views.lista_contactos),
           
]
