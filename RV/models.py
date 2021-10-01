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


class AnswersKeys(models.Model):
    runa_1runa_7 = models.CharField(max_length=20)
    runa_1runa_6 = models.CharField(max_length=20)
    runa_1runa_5 = models.CharField(max_length=20)
    runa_1runa_4 = models.CharField(max_length=20)
    runa_1runa_3 = models.CharField(max_length=20)
    runa_1runa_2 = models.CharField(max_length=20)
    runa_2runa_7 = models.CharField(max_length=20)
    runa_2runa_6 = models.CharField(max_length=20)
    runa_2runa_5 = models.CharField(max_length=20)
    runa_2runa_4 = models.CharField(max_length=20)
    runa_2runa_3 = models.CharField(max_length=20)
    runa_3runa_7 = models.CharField(max_length=20)
    runa_3runa_6 = models.CharField(max_length=20)
    runa_3runa_5 = models.CharField(max_length=20)
    runa_3runa_4 = models.CharField(max_length=20)
    runa_4runa_7 = models.CharField(max_length=20)
    runa_4runa_6 = models.CharField(max_length=20)
    runa_4runa_5 = models.CharField(max_length=20)
    runa_5runa_7 = models.CharField(max_length=20)
    runa_5runa_6 = models.CharField(max_length=20)
    runa_6runa_7 = models.CharField(max_length=20)

    runa_7runa_1 = models.CharField(max_length=20)
    runa_6runa_1 = models.CharField(max_length=20)
    runa_5runa_1 = models.CharField(max_length=20)
    runa_4runa_1 = models.CharField(max_length=20)
    runa_3runa_1 = models.CharField(max_length=20)
    runa_2runa_1 = models.CharField(max_length=20)
    runa_7runa_2 = models.CharField(max_length=20)
    runa_6runa_2 = models.CharField(max_length=20)
    runa_5runa_2 = models.CharField(max_length=20)
    runa_4runa_2 = models.CharField(max_length=20)
    runa_3runa_2 = models.CharField(max_length=20)
    runa_7runa_3 = models.CharField(max_length=20)
    runa_6runa_3 = models.CharField(max_length=20)
    runa_5runa_3 = models.CharField(max_length=20)
    runa_4runa_3 = models.CharField(max_length=20)
    runa_7runa_4 = models.CharField(max_length=20)
    runa_6runa_4 = models.CharField(max_length=20)
    runa_5runa_4 = models.CharField(max_length=20)
    runa_7runa_5 = models.CharField(max_length=20)
    runa_6runa_5 = models.CharField(max_length=20)
    runa_7runa_6 = models.CharField(max_length=20)

    rv_answers_keys = models.OneToOneField(RunicheskiyVosk, on_delete=models.CASCADE, primary_key=True)

class ManticKeys(models.Model):
    # ManyToManyField
    value_keys = models.CharField(max_length=20)# 'fehuuruz'
    value_name = models.CharField(max_length=20)# 'Феху - Уруз'
    value_mantic = models.CharField(max_length=200)# мантическое значение в гадании
    value_protection = models.CharField(max_length=200)# мантическое значение в сфере защиты
    mantic_answers = models.ManyToManyField(AnswersKeys)
