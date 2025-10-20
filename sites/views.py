# sites/views.py
from rest_framework import viewsets
from .models import Site
from .serializers import SiteSerializer

class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'role'):
            if user.role == 'admin':
                return Site.objects.select_related('company')
            elif user.role in ['technician', 'client']:
                return Site.objects.filter(company=user.company).select_related('company')
        return Site.objects.none()