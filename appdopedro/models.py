from django.db import models

class Estatisticas(models.Model):
  categoria = models.CharField(max_length=50)
  numeros =  models.IntegerField()

class Dias(models.Model):
  OPTIONS = [
    ("A", "Muito Marcante"),
    ("M", "Marcante"),
    ("N", "Nem tão marcante"),
  ]
  descricao = models.CharField(max_length=50)
  ano = models.IntegerField()
  impacto = models.CharField(max_length=1, choices=OPTIONS)

class Fred(models.Model):
  informacoes = models.CharField(max_length=15)
  

# Create your models here.
