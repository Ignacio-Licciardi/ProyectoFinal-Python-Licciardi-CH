from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=40, default="Mensaje")
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.now)