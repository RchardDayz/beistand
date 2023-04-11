from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto
from inicio.forms import CreacionFormularioContacto

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
                name=datos_correctos['id'], 
                phone=datos_correctos['id'], 
                email=datos_correctos['id'],
                message=datos_correctos['id'],
                )
            datos.save()
            
            return redirect('inicio:lista_contactos')
        
    formulario = CreacionFormularioContacto()
    return render(request, r'inicio/contacto.html', {'formulario': formulario})

def lista_contactos(request):
        return render(request, r'inicio/lista_contactos.html')

