from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=240)
    autor = models.CharField(max_length=40,default="User")
    fecha = models.DateField(default=datetime.now)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
        return self.titulo 