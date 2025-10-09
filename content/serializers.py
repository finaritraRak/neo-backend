from rest_framework import serializers
from .models import PageContent

class PageContentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = PageContent
        fields = [
            'id', 'page', 'title', 'content_type', 'content', 'image',
            'status', 'author_name', 'created_at', 'updated_at', 'views'
        ]
        read_only_fields = ['id', 'author_name', 'created_at', 'updated_at', 'views']
