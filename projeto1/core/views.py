from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ExemploSerializer
from .models import Exemplo

class ExemploViewSet(viewsets.ModelViewSet):
    queryset = Exemplo.objects.all()
    serializer_class = ExemploSerializer
