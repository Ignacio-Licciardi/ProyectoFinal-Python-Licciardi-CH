from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserEditForm , AvatarForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import DatosUsuario
import os
# Create your views here.

#Registro de usuario 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, 'accounts/success.html', {'form':form,'mensaje':f"Usuario Creado:  {username}. Inicie Sesion"})
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})



# Inicio de sesión
def login_user(request):

    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid:
            user= request.POST['username']
            key= request.POST['password']
            
            user_1 = authenticate(username=user, password=key)
            
            if user_1 is not None:
                login(request, user_1)
                return render(request, 'accounts/success.html', {'form':form,'mensaje':f"Usuario Logueado: {user_1}"})
            else:
                return render(request, 'accounts/login.html', {'form':form,'mensaje':f"Usuario o clave incorrectos"})
        else:
            return render(request, 'accounts/login.html', {'form':form,'mensaje':f"FORMULARIO INVALIDO"})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})




# Edición de Usuario
@login_required
def edit_profile(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, request.FILES)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            if informacion.get('first_name'):
                usuario.first_name=informacion.get('first_name')
            if informacion.get('last_name'):
                usuario.last_name=informacion.get('last_name')
            if informacion.get('email'):
                usuario.email=informacion.get('email')
            if informacion.get('password_1') and informacion.get('password_1') == informacion.get('password_2'):
                usuario.set_password(informacion.get('password_1'))
            usuario.save()

            return render(request, 'accounts/success.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
        else:
            return render(request, 'accounts/edit_profile.html', {'formulario':formulario})

    formulario=UserEditForm(
        initial={
            'email':usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
        }
    )

    return render(request, 'accounts/edit_profile.html', {'formulario':formulario})
#Cierre de sesion

@login_required
def logout_user(request):
    return render(request,'accounts/logout.html')


#Agregar avatares

@login_required
def add_avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid() and len(request.FILES) != 0 :
            image = request.FILES['image']
            avatar_v = DatosUsuario.objects.filter(user=request.user.id)
            if not avatar_v.exists():
                avatar_n = DatosUsuario(user=request.user, avatar=image)
            else:
                avatar_n = avatar_v[0]
                if len(avatar_n.avatar) > 0:
                    os.remove(avatar_n.avatar.path)
                avatar_n.avatar = image
            avatar_n.save()
            return render(request, 'accounts/success.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})


    formulario=AvatarForm()
    return render(request, 'accounts/add_avatar.html', {'formulario':formulario, 'usuario':request.user})


def about(request):
    return render(request,"accounts/about.html")

def success(request):
    return render(request,"accounts/success.html")
    
