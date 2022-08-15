from django.shortcuts import render

from accounts.models import DatosUsuario


def index(request):
    avatares = DatosUsuario.objects.filter(user = request.user.id)
    if avatares.exists():
        return render(request,"accounts/index.html", {"url":avatares[0].avatar.url})
    else:
        return render(request, "accounts/index.html")
