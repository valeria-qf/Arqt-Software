from django.shortcuts import render
from rest_framework.decorators import action
# Create your views here.
from rest_framework import viewsets
from .serializers import AlunoSerializer
from .models import Aluno
from rest_framework.response import Response

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
