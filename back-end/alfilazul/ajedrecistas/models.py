from django.db import models

# Create your models here.
class Ajedrecista(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    ranking_local = models.IntegerField(default=0)
    sexo = models.CharField(max_length=1)
    escuela = models.CharField(max_length=150)
    club = models.CharField(max_length=150)
    email = models.EmailField(max_length=75)
    bird_date = models.DateTimeField('Bird Date')

