from django.db import models
#from django.conf import settings
from projeto import settings

class Dibre(models.Model):
    autor = models.CharField(max_length=20)
    nomeProjeto = models.CharField(max_length=20)
    linguagem = models.CharField(max_length=20)

    
