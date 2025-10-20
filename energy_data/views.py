# energy_data/views.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import EnergyReading
from .serializers import EnergyReadingSerializer

class EnergyReadingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API pour lire les données énergétiques.
    Seuls les utilisateurs authentifiés peuvent y accéder.
    """
    serializer_class = EnergyReadingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['site', 'site__company', 'is_valid']
    ordering_fields = ['timestamp', 'created_at']
    ordering = ['-timestamp']

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'role'):
            if user.role == 'admin':
                return EnergyReading.objects.select_related('site', 'site__company')
            elif user.role in ['technician', 'client']:
                return EnergyReading.objects.filter(
                    site__company=user.company
                ).select_related('site', 'site__company')
        return EnergyReading.objects.none()