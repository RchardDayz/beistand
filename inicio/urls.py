
from django.urls import path
from inicio import views

# app_name = 'inicio'

urlpatterns = [
    path('', views.inicio),
    # path('contact/', views.contacto),
    
    
]
