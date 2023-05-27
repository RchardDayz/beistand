from django.contrib import admin
from usuarios.models import CustomUser, InformacionExtra
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(InformacionExtra)
admin.site.register(CustomUser, UserAdmin)