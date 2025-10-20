# alarms/serializers.py
from rest_framework import serializers
from .models import Alarm

class AlarmSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)
    company_name = serializers.CharField(source='site.company.name', read_only=True)
    reading_timestamp = serializers.DateTimeField(source='reading.timestamp', read_only=True)

    class Meta:
        model = Alarm
        fields = [
            'id',
            'site',
            'site_name',
            'company_name',
            'reading',
            'reading_timestamp',
            'alarm_type',
            'description',
            'is_active',
            'severity',
            'triggered_at',
            'resolved_at'
        ]
        read_only_fields = ['triggered_at']