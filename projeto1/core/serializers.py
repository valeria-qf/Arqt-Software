from rest_framework import serializers
from .models import Aluno, Nota

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'aluno', 'valor']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome']