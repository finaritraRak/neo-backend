# notifications/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import Notification
from .serializers import NotificationSerializer

User = get_user_model()


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')


# ✅ Nouvelle vue : Détail d'une notification
class NotificationDetailView(generics.RetrieveAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


class MarkNotificationAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

    def patch(self, request, *args, **kwargs):
        try:
            notification = self.get_object()
            if notification.is_read:
                return Response(NotificationSerializer(notification).data, status=status.HTTP_200_OK)
            notification.is_read = True
            notification.save(update_fields=['is_read'])
            return Response(NotificationSerializer(notification).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'Impossible de marquer comme lu', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MarkAllNotificationsAsReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
            return Response({'status': 'all marked as read'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'Échec du marquage global', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(['GET'])
def unread_notifications_count(request):
    if not request.user.is_authenticated:
        return Response({'count': 0})
    count = Notification.objects.filter(recipient=request.user, is_read=False).count()
    return Response({'count': count})



class DeleteNotificationView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            notification = self.get_object()
            notification.delete()
            return Response({'status': 'deleted'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'Échec de suppression', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DeleteMultipleNotificationsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        if not ids:
            return Response({'error': 'Aucun ID fourni'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Notification.objects.filter(recipient=request.user, id__in=ids).delete()
            return Response({'status': 'deleted', 'count': len(ids)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'Échec de suppression multiple', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )