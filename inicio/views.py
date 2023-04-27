from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto, Producto
from inicio.forms import CreacionFormularioProducto, BuscarProducto, ModificarFormularioProducto, MostrarFormularioProducto, BaseFormularioContacto
from django.views.generic import TemplateView
from datetime import datetime
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def vista_principal(request):
    return render(request, 'inicio/index.html')

#=======================================================================================
#=======================================================================================

class CrearProducto(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "inicio/crear_producto.html"
    success_url= reverse_lazy('inicio:lista_productos')
    fields= ['nombre', 'fecha_alta', 'cant_pzas', 'descripcion']

#=======================================================================================
#=======================================================================================

class ListaProductos(ListView):
    model = Producto
    template_name = "inicio/lista_productos.html"

#=======================================================================================
#=======================================================================================


class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "inicio/eliminar_producto.html"
    success_url= reverse_lazy('inicio:lista_productos.html')

#=======================================================================================
#=======================================================================================
    

class ModificarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "inicio/modificar_producto.html"
    success_url= reverse_lazy("inicio:lista_producto/")
    fields= ['nombre', 'fecha_alta', 'cant_pazas', 'descripcion']

#=======================================================================================
#=======================================================================================
    

class about(TemplateView):
    template_name = "inicio/about.html"

#=======================================================================================
#=======================================================================================
    
class servicios(TemplateView):
    template_name = "inicio/servicios.html"

#=======================================================================================
#=======================================================================================
    
class investigaciones(TemplateView):
    template_name = "inicio/investigaciones2.html"

#=======================================================================================
#=======================================================================================
    
def crear_contacto(request):
    if request.method == 'POST':
        formulario = BaseFormularioContacto(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            datos = contacto(
                name=datos_correctos['name'], 
                phone=datos_correctos['phone'], 
                email=datos_correctos['email'],
                message=datos_correctos['message'],
                )
            datos.save()
            
            return redirect('inicio:lista_contactos')
        
    formulario = BaseFormularioContacto()
    return render(request, 'inicio/contacto.html', {'formulario': formulario})

#=======================================================================================
#=======================================================================================
    
class MostrarFormularioProducto(DetailView):
    model = Producto
    template_name = 'inicio/mostrar_producto.html'



