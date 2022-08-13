from django.shortcuts import render

from accounts.models import DatosUsuario


def index(request):
    
    avatares = DatosUsuario.objects.filter(user = request.user.id)

    return render(request,"index.html", {"url":avatares[0].avatar.url})