from django.shortcuts import render

from accounts.models import DatosUsuario


def index(request):
    if (request.user.id == True) and (DatosUsuario.avatar != None):
        avatares = DatosUsuario.objects.filter(user = request.user.id)
        return render(request,"index.html", {"url":avatares[0].avatar.url})
    else:
        return render(request, "index.html")