from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto
from inicio.forms import CreacionFormularioContacto, BuscarContacto, ModificarFormularioContacto
from django.views.generic import TemplateView


# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')

# Machote de la funcion
def crear_contacto(request):
    if request.method == 'POST':
        formulario = CreacionFormularioContacto(request.POST)
        
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
        
    formulario = CreacionFormularioContacto()
    return render(request, r'inicio/contacto.html', {'formulario': formulario})

def lista_contactos(request):
    nombre_a_buscar = request.GET.get('name', None)
    
    if nombre_a_buscar:
        contactos = contacto.objects.filter(name__icontains=nombre_a_buscar)
    else:
        contactos = contacto.objects.all()
    
    formulario_busqueda = BuscarContacto()
    return render(request, r'inicio/lista_contactos.html', {'contactos': contactos})

def eliminar_contacto(request, id):
    contacto_a_eliminar = contacto.objects.get(id=id)
    contacto_a_eliminar.delete()
    return redirect('inicio:lista_contactos')

def modificar_contacto(request, id):
    contacto_a_modificar = contacto.objects.get(id=id)
    if request.method == 'POST':
        formulario = ModificarFormularioContacto(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            
            contacto_a_modificar.name = data_limpia['name']
            contacto_a_modificar.phone = data_limpia['phone']
            contacto_a_modificar.email = data_limpia['email']
            contacto_a_modificar.message = data_limpia['message']
            
            contacto_a_modificar.save()
            return redirect('inicio:lista_contactos')
        else:
            return render(request, 'inicio/modificar_contacto.html', {'formulario': formulario, 'id':id})
           
    formulario = ModificarFormularioContacto(initial={
        'name':  contacto_a_modificar.name,
        'phone':  contacto_a_modificar.phone,
        'email':  contacto_a_modificar.email,
        'message':  contacto_a_modificar.message,
    })
    return render(request, 'inicio/modificar_contacto.html', {'formulario': formulario, 'id':id})

class about(TemplateView):
    template_name = "inicio/about.html"
    
class servicios(TemplateView):
    template_name = "inicio/servicios.html"
    
class investigaciones(TemplateView):
    template_name = "inicio/investigaciones2.html"



