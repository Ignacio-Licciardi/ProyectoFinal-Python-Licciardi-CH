from django.urls import path
from .views import register , login_user ,editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='../templates/logout.html'), name='logout'),
    path('login/',login_user, name= 'login'),
    path('profile/', editar_perfil, name='editar_perfil'),
]
