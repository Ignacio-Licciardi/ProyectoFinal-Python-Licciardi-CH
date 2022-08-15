from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=240)


    def __str__(self):
        return self.titulo 