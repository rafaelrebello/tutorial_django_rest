from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    body = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo