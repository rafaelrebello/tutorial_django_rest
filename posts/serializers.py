#   posts/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'autor', 'titulo', 'body', 'data_criacao')
        model = Post