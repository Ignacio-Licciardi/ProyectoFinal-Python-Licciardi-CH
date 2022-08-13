from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class DatosUsuario(models.Model):
    
    # Usando el modelo User de Django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    
