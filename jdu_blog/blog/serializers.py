from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Barcha maydonlarni (id, title, category, content, image, created_at...) JSON qilish
        