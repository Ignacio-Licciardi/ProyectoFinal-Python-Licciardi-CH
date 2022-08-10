from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class DatosUsuario(models.Model):
    
    # Usando el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
