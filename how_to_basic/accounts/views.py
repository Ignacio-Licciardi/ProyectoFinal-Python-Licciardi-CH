from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import DatosUsuario
# Create your views here.

#Registro de usuario 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, 'index.html', {'form':form,'mensaje':f"Usuario Creado:  {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})



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
                return render(request, 'index.html', {'form':form,'mensaje':f"Bienvenido {user_1}"})
            else:
                return render(request, 'login.html', {'form':form,'mensaje':f"Usuario o clave incorrectos"})
        else:
            return render(request, 'login.html', {'form':form,'mensaje':f"FORMULARIO INVALIDO"})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})





#Edicion de usuario 

@login_required
def editar_perfil(request):
    usuario=request.user
    datos_usuario=DatosUsuario.objects.get_or_create(user=usuario)

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
            #if informacion.get('avatar'):
                #datos_usuario.avatar=informacion.get('avatar')
            if  informacion.get('password_1') == informacion.get('password_2'):
                usuario.set_password(informacion.get('password_1'))
            #datos_usuario.save()
            usuario.save()

            return redirect(request, 'index.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
        else:
            return render(request, 'edit_profile.html', {'formulario':formulario})

    formulario=UserEditForm(
        initial={
            'email':usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            #'avatar': datos_usuario.avatar
        }
    )

    return render(request, 'edit_profile.html', {'formulario':formulario})

#Cierre de sesion

@login_required
def logout_user(request):
    return render(request,'logout.html')
