from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import filters

class Aluno(models.Model):
    nome = models.CharField(max_length=200, null=True)

    nota1 = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2, null=True)
    nota2 = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2, null=True)
    nota3 = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2, null=True)
    nota4 = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2, null=True
    )
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

    @property
    def media(self):
        notas_aluno = [self.nota1, self.nota2, self.nota3, self.nota4]
        if all(nota is not None for nota in notas_aluno):
            total_notas = sum(notas_aluno)
            media = total_notas / 4
            return media
        return None


@receiver(post_save, sender=Aluno)
def atualizar_media_aluno(sender, instance, **kwargs):
    instance.media