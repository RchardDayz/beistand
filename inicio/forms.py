from django import forms


class CreacionFormularioContacto(forms.Form):
    name = forms.CharField(max_length=20)
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    message = forms.CharField(max_length=500)
    
class BuscarContacto(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    

class ModificarFormularioContacto(forms.Form):
    name = forms.CharField(max_length=20)
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    message = forms.CharField(max_length=500)