from django.shortcuts import render, redirect
# from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import contacto

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')

# Machote de la funcion
# def contacto(request):
#     datos = contacto{
#         'name': name,
#         'empresa': empresa,
#         'phone': phone,
#         'domicilio': domicilio,
#         'colonia': colonia,
#         'ciudad': ciudad,
#         'estado': estado,
#         'pais': pais,
#         'c_p': c_p,
#         'email': email,
#         'message': message,
#     }
#     return render(request, r'contact.html', datos)
