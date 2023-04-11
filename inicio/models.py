from django.db import models

# Create your models here.

class contacto(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)
    
    
    
    