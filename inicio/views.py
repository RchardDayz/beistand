from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto, Producto
from inicio.forms import CreacionFormularioProducto, BuscarProducto, ModificarFormularioProducto, MostrarFormularioProducto, BaseFormularioContacto
from django.views.generic import TemplateView
from datetime import datetime
from django.urls import reverse_lazy


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def vista_principal(request):
    return render(request, 'inicio/index.html')

# Machote de la funcion
def crear_producto(request):
    if request.method == 'POST':
        formulario = CreacionFormularioProducto(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            datos = Producto(
                nombre=datos_correctos['nombre'], 
                fecha_alta=datos_correctos['fecha'], 
                cant_pzas=datos_correctos['cant_pzas'],
                descripcion=datos_correctos['descripcion'],
                )
            datos.save()
            
            return redirect('inicio:lista_productos')
        
    formulario = CreacionFormularioProducto()
    return render(request, 'inicio/lista_productos.html', {'formulario': formulario})

def lista_productos(request):
    nombre_a_buscar = request.GET.get('name', None)
    
    if nombre_a_buscar:
        productos = Producto.objects.filter(name__icontains=nombre_a_buscar)
    else:
        productos = Producto.objects.all()
    
    formulario_busqueda = BuscarProducto()
    return render(request, 'inicio/lista_productos.html', {'producto': productos, 'formulario': formulario_busqueda})


class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "inicio/eliminar_producto.html"
    success_url= reverse_lazy('inicio:lista_productos.html')
    

class ModificarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "inicio/modificar_producto.html"
    success_url= reverse_lazy("inicio:lista_producto/")
    fields= ['nombre', 'fecha_alta', 'cant_pazas', 'descripcion']
    

class about(TemplateView):
    template_name = "inicio/about.html"
    
class servicios(TemplateView):
    template_name = "inicio/servicios.html"
    
class investigaciones(TemplateView):
    template_name = "inicio/investigaciones2.html"
    
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

    
class MostrarFormularioProducto(DetailView):
    model = Producto
    template_name = 'inicio/mostrar_producto.html'



