# alarms/views.py
from rest_framework import viewsets
from .models import Alarm
from .serializers import AlarmSerializer

class AlarmViewSet(viewsets.ModelViewSet):
    serializer_class = AlarmSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'role'):
            if user.role == 'admin':
                return Alarm.objects.select_related('site', 'site__company', 'reading')
            elif user.role in ['technician', 'client']:
                return Alarm.objects.filter(
                    site__company=user.company
                ).select_related('site', 'site__company', 'reading')
        return Alarm.objects.none()