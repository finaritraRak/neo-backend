# companies/views.py
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Seuls les admins peuvent voir toutes les entreprises.
    Les technicians/clients ne voient que leur propre entreprise.
    Lecture seule pour tous (pas de création/modif via cette API).
    """
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'role'):
            if user.role == 'admin':
                return Company.objects.all()
            elif user.role in ['technician', 'client']:
                return Company.objects.filter(id=user.company_id)
        return Company.objects.none()