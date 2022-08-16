from django import forms
from django.contrib.auth.models import User



class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=240)
    autor = forms.CharField(max_length=40)
    fecha = forms.DateField()
    imagen = forms.ImageField()

