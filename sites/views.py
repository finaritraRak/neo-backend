# sites/views.py
class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Site.objects.all()
        elif user.role == 'technician' or user.role == 'client':
            return Site.objects.filter(company=user.company)
        return Site.objects.none()