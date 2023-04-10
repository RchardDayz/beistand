from django.shortcuts import render, redirect
# from django.template import template, Context, loader
from django.http import HttpResponse
# from inicio.models import contacto

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')

#Machote de la funcion
# def nombre_de_la_funcion(request):
#     datos = contacto{
#         'nombre': nombre,
#         'apellido': apellido,
#         'empresa': empresa,
#         'telefono': telefono,
#         'domicilio': domicilio,
#         'colonia': colonia,
#         'ciudad': ciudad,
#         'estado': estado,
#         'pais': pais,
#         'c_p': c_p,
#         'e_mail': e_mail
#     }
#     return render(request, r'inicio/nombre_del_template.html', datos)
