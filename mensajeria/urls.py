from django.urls import path
from . import views

app_name = 'mensajeria'

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuario/<int:usuario_id>/mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
]