from django.db import models

# Create your models here.

class Exemplo(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome