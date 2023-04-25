from django.contrib import admin
from inicio.models import contacto, Producto


# Register your models here.

admin.site.register([Producto, contacto])

