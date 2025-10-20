# companies/serializers.py
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'domain', 'country', 'created_at']
        read_only_fields = ['created_at']