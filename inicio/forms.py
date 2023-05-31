from django import forms


class BaseFormularioContacto(forms.Form):
    name = forms.CharField(max_length=20)
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    message = forms.CharField(max_length=500)
    
class BaseFormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha_alta = forms.DateField()
    cant_pzas = forms.IntegerField(required=False)
    descripcion = forms.Textarea()
    imagen = forms.ImageField(required=False)
    
class MostrarFormularioProducto(BaseFormularioProducto):
    ...
    
class CreacionFormularioProducto(BaseFormularioProducto):
    ...
    
class BuscarProducto(BaseFormularioProducto):
       nombre = forms.CharField(max_length=20, required=False)  


class ModificarFormularioProducto(BaseFormularioProducto):
    ...