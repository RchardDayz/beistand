from django.contrib import admin
from usuarios.models import InformacionExtra
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

admin.site.register(InformacionExtra)
admin.site.register(CustomUser, UserAdmin)