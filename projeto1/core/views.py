from django.shortcuts import render
from rest_framework.decorators import action
# Create your views here.
from rest_framework import viewsets
from .serializers import AlunoSerializer, NotasSerializer, DisciplinaSerializer
from .models import Aluno, Nota, Disciplina
from rest_framework.response import Response

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotasSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer