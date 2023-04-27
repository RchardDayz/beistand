from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from usuarios.models import InformacionExtra
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.forms import MiFormularioDeCreacion, EdicionDatosUsuario

# Create your views here.

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            InformacionExtra.objects.get_or_create(user=request.user)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/login.html', {'formulario': formulario})
            
#===========================================================================================    
#===========================================================================================
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == "POST":
        formulario = MiFormularioDeCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})
            
    formulario = MiFormularioDeCreacion()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

#===========================================================================================
#===========================================================================================

@login_required
def editar_perfil(request):
    if request.method == "POST":
        formulario = EdicionDatosUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                request.user.informacionextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.informacionextra.save()
            formulario.save()
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})
            
    formulario = EdicionDatosUsuario(initial={'avatar': request.user.informacionextra.avatar}, instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})
    
#================================================================================================================
#================================================================================================================

class CambioContrasenia(LoginRequiredMixin,PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuarios:editar_perfil')