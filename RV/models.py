from django.db import models
from .futark import Futark

# Create your models here.
class RunicheskiyVosk(models.Model):
    runa_1 = models.CharField(max_length=15, choices=Futark.futark)
    runa_2 = models.CharField(max_length=15, choices=Futark.futark)
    runa_3 = models.CharField(max_length=15, choices=Futark.futark)
    runa_4 = models.CharField(max_length=15, choices=Futark.futark)
    runa_5 = models.CharField(max_length=15, choices=Futark.futark)
    runa_6 = models.CharField(max_length=15, choices=Futark.futark)
    runa_7 = models.CharField(max_length=15, choices=Futark.futark)

    
