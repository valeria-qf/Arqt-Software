from django.shortcuts import render
from rest_framework.decorators import action
# Create your views here.
from rest_framework import viewsets
from .serializers import AlunoSerializer, NotasSerializer
from .models import Aluno, Nota
from rest_framework.response import Response

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=True, methods=['get'])
    def calcular_media(self, request, pk=None):
        aluno = self.get_object()
        media = aluno.calcular_media()
        return media

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotasSerializer