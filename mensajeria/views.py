from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Mensaje
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mensajeria/index.html', {'usuarios': usuarios})

@login_required
def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    return render(request, 'mensajeria/detalle_usuario.html', {'usuario': usuario})

@login_required
def enviar_mensaje(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    mensaje = request.POST['mensaje']
    # Aquí se implementa la lógica para guardar el mensaje en la base de datos
    return HttpResponse(f"Mensaje enviado a {usuario.nombre}: {mensaje}")
