from django.contrib import admin
from inicio.models import contacto, Clientes


# Register your models here.

admin.site.register([Clientes, contacto])

