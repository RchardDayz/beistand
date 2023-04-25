
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.vista_principal, name='inicio'),
    path('crear/producto/', views.crear_producto, name='crear_producto'),
    path('producto/lista-productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/<int:id>/modificar/', views.modificar_producto, name='modificar_producto'),
    
    path('producto/<int:pk>/mostrar/', views.MostrarFormularioProducto.as_view(), name='mostrar_producto'),
    path('about/', views.about.as_view(), name= 'about'),
    path('servicios/', views.servicios.as_view(), name= 'servicios'),
    path('investigaciones2/', views.investigaciones.as_view(), name= 'investigaciones'),
    path('contacto/', views.crear_contacto, name= 'contacto'),
]
