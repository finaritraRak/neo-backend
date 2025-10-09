# settings/serializers.py
from rest_framework import serializers
from .models import SiteSettings

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        
    def to_representation(self, instance):
        # Mapping des noms de champs backend vers frontend
        data = super().to_representation(instance)
        field_mapping = {
            'site_name': 'siteName',
            'site_description': 'siteDescription',
            'contact_email': 'contactEmail',
            'timezone': 'timezone',
            'language': 'language',
            'theme': 'theme',
            'email_notifications': 'emailNotifications',
            'push_notifications': 'pushNotifications',
            'weekly_reports': 'weeklyReports',
            'two_factor_auth': 'twoFactorAuth',
            'session_timeout': 'sessionTimeout',
            'password_expiry': 'passwordExpiry'
        }
        
        # Convertir les noms de champs
        converted_data = {}
        for backend_key, value in data.items():
            frontend_key = field_mapping.get(backend_key, backend_key)
            converted_data[frontend_key] = value
            
        return converted_data