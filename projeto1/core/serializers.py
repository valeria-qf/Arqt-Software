from rest_framework import serializers
from .models import Aluno, Nota, Disciplina

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'aluno', 'disciplina', 'valor']

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome']

class AlunoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'media']

    def get_media(self, obj):
        return obj.media
