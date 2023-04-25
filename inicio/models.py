from django.db import models

# Create your models here.

class contacto(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return f'nombre {self.name}, Telefono {self.phone}, e-mail {self.email}, mensaje {self.message}'
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_alta = models.DateField()
    cant_pzas = models.IntegerField(null=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f'Productos {self.nombre} {self.fecha_alta} {self.cant_pzas} {self.descripcion}'
    