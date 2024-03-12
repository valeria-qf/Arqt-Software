from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from rest_framework.response import Response


class Aluno(models.Model):
    nome = models.CharField(max_length = 200)

    def calcular_media(self):
        notas_aluno = self.nota_set.all()
        if notas_aluno.exists():
            total_notas = sum(nota.valor for nota in notas_aluno)
            media = total_notas / len(notas_aluno)
            return Response({'media': media})
        return 0.0


class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    valor = models.DecimalField(
        validators = [MinValueValidator(0), MaxValueValidator(100)],
        max_digits = 5,
        decimal_places = 2
        )