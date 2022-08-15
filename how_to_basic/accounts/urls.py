
from django.urls import path
from .views import add_avatar, edit_profile, prueba_template, register , login_user 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('login/',login_user, name= 'login'),
    path('profile/', edit_profile, name='edit_profile'),
    path('addAvatar/', add_avatar, name='add_avatar'),
    path('prueba_template/', prueba_template, name='prueba_template'),
]
