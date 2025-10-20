# sites/serializers.py
from rest_framework import serializers
from .models import Site

class SiteSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Site
        fields = [
            'id',
            'name',
            'company',
            'company_name',
            'topology',
            'location',
            'is_active',
            'created_at'
        ]
        read_only_fields = ['created_at']