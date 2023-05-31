from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class contacto(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return f'nombre: {self.name}, Telefono: {self.phone}, e-mail: {self.email}, mensaje: {self.message}'
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_alta = models.DateField()
    cant_pzas = models.IntegerField(null=True)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    
    def __str__(self):
        return f'Producto: {self.nombre}, Fecha de Alta: {self.fecha_alta}, Cantidad de Piezas: {self.cant_pzas}, Descripcion: {self.descripcion}, Imagen: {self.imagen}'
    