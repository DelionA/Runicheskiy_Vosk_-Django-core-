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


class ManticKeys(models.Model):
    # ManyToManyField
    value_keys = models.CharField(max_length=20)# 'fehuuruz'
    value_name = models.CharField(max_length=20)# 'Феху - Уруз'
    value_mantic = models.CharField(max_length=200)# мантическое значение в гадании
    value_protection = models.CharField(max_length=200)# мантическое значение в сфере защиты
    mantic_answers = models.ManyToManyField(RunicheskiyVosk)
