from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'nota1', 'nota2', 'nota3', 'nota4' , 'media']

    def get_media(self, obj):
        return obj.media
