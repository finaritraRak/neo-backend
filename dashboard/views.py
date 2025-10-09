# dashboard/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from apps.users.models import User 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    total_users = User.objects.count()
    active_users = User.objects.filter(status='active').count()
    stats = {
        'totalUsers': total_users,
        'activeUsers': active_users,
        'totalRevenue': 45892,
        'monthlyGrowth': 12.5,
        'newRegistrations': User.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=30)
        ).count(),
        'conversionRate': 3.2,
    }
    return Response(stats)
