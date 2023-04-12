from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto
from inicio.forms import CreacionFormularioContacto, BuscarContacto

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

