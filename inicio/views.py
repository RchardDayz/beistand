from django.shortcuts import render
from django.template import template, Context, loader
from django.http import HttpResponse

# Create your views here.

#Machote de la funcion
def nombre_de_la_funcion(request):
    
    template = loader.get_template(r'nombre_del_template.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)
