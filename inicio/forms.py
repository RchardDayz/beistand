from django import forms


class BaseFormularioContacto(forms.Form):
    name = forms.CharField(max_length=20)
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    message = forms.CharField(max_length=500)
    
class CreacionFormularioContacto(BaseFormularioContacto):
    ...
    
class BuscarContacto(BaseFormularioContacto):
       name = forms.CharField(max_length=20, required=False)

    

class ModificarFormularioContacto(BaseFormularioContacto):
    ...