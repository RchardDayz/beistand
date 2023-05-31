from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    github_repo = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username

class InformacionExtra(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'Usuario: {self.user}, Imagen: {self.avatar}'
    
