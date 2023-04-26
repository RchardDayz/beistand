
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.vista_principal, name='inicio'),
    path('productos/', views.ListaProductos.as_view(), name='lista_productos'),
    path('productos/crear/', views.CrearProducto.as_view(), name='crear_producto'),
    path('productos/<int:pk>/mostrar/', views.MostrarFormularioProducto.as_view(), name='mostrar_producto'),
    path('productos/<int:pk>/eliminar/', views.EliminarProducto.as_view(), name='eliminar_producto'),
    path('productos/<int:pk>/modificar/', views.ModificarProducto.as_view(), name='modificar_producto'),
    path('about/', views.about.as_view(), name= 'about'),
    path('servicios/', views.servicios.as_view(), name= 'servicios'),
    path('investigaciones2/', views.investigaciones.as_view(), name= 'investigaciones'),
    path('contacto/', views.crear_contacto, name= 'contacto'),
]
