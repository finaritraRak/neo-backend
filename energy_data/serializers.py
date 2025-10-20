# energy_data/serializers.py
from rest_framework import serializers
from .models import EnergyReading

class EnergyReadingSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)
    company_name = serializers.CharField(source='site.company.name', read_only=True)

    class Meta:
        model = EnergyReading
        fields = [
            'id',
            'site',
            'site_name',
            'company_name',
            'timestamp',
            'total_load_kwh',
            'genset_kwh',
            'pv_production_kwh',
            'battery_kwh',
            'pv_theoretical_kwh',
            'is_valid',
            'created_at'
        ]