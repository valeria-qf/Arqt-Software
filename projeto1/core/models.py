from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver

class Aluno(models.Model):
    nome = models.CharField(max_length = 200)

    @property
    def media(self):
        notas_aluno = self.nota_set.all()
        if notas_aluno.count() == 4:
            total_notas = sum(nota.valor for nota in notas_aluno)
            media = total_notas / 4
            return media
        return None

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)


class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    valor = models.DecimalField(
        validators = [MinValueValidator(0), MaxValueValidator(100)],
        max_digits = 5,
        decimal_places = 2
        )
    
@receiver(post_save, sender=Nota)
def atualizar_media_aluno(sender, instance, **kwargs):
    aluno = instance.aluno
    aluno.media
