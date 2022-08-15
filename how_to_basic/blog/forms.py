from django import forms
from django.contrib.auth.models import User



class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=240)


