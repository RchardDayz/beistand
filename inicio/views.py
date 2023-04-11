from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')

# Machote de la funcion
def contacto(request):
    if request.method == 'POST':
        datos = contacto(
            name=request.POST['id'], 
            phone=request.POST['id'], 
            email=request.POST['id'],
            message=request.POST['id'],
            )
        datos.save()
    return render(request, r'inicio/contact.html', datos)
