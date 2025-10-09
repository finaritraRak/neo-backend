# settings/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import SiteSettings, UserProfile
from .serializers import SiteSettingsSerializer
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    return JsonResponse({"message": "Settings API ready"})

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def site_settings_view(request):
    settings_obj, created = SiteSettings.objects.get_or_create(id=1)

    if request.method == 'GET':
        serializer = SiteSettingsSerializer(settings_obj)
        return Response(serializer.data)

    elif request.method == 'POST':
       
        data = {}
        
     
        for key, value in request.data.items():
            data[key] = value
            
       
        field_mapping = {
            'siteName': 'site_name',
            'siteDescription': 'site_description',
            'contactEmail': 'contact_email',
            'timezone': 'timezone',
            'language': 'language',
            'theme': 'theme',
            'emailNotifications': 'email_notifications',
            'pushNotifications': 'push_notifications',
            'weeklyReports': 'weekly_reports',
            'twoFactorAuth': 'two_factor_auth',
            'sessionTimeout': 'session_timeout',
            'passwordExpiry': 'password_expiry'
        }
        
   
        converted_data = {}
        for frontend_key, value in data.items():
            backend_key = field_mapping.get(frontend_key, frontend_key)
            
            if backend_key in ['email_notifications', 'push_notifications', 'weekly_reports', 'two_factor_auth']:
                if isinstance(value, str):
                    converted_data[backend_key] = value.lower() == 'true'
                else:
                    converted_data[backend_key] = bool(value)
         
            elif backend_key in ['session_timeout', 'password_expiry']:
                try:
                    converted_data[backend_key] = int(value)
                except (ValueError, TypeError):
                    converted_data[backend_key] = 30 if backend_key == 'session_timeout' else 90
            else:
                converted_data[backend_key] = value
        
       
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            converted_data['profile_image'] = profile_image
        
        serializer = SiteSettingsSerializer(settings_obj, data=converted_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) 
def user_profile_view(request):
  
    if request.method == 'GET':
      
        user_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'bio': '',
            'profile_image': None
        }
        return Response(user_data)

    elif request.method == 'POST':
      
        user_data = {
            'first_name': request.data.get('first_name', ''),
            'last_name': request.data.get('last_name', ''),
            'email': request.data.get('email', ''),
            'bio': request.data.get('bio', ''),
            'profile_image': None
        }
        return Response(user_data)