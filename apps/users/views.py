# apps/users/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from .models import User, PasswordResetToken
from .serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.check_password(password):
        return Response({'error': 'Mot de passe invalide'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    return Response({
        'token': str(refresh.access_token),
        'refresh': str(refresh),
        'user': UserSerializer(user, context={'request': request}).data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    return Response(UserSerializer(request.user, context={'request': request}).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    return Response({"message": "Déconnecté"})


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


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email requis'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Cet email n’est associé à aucun compte.'}, status=status.HTTP_404_NOT_FOUND)

    PasswordResetToken.objects.filter(user=user).delete()

    reset_token = PasswordResetToken.objects.create(user=user)

    frontend_url = getattr(settings, 'FRONTEND_URL', 'https://dev.calm-adventure-tours.com').strip()
    reset_link = f"{frontend_url}/reset-password?token={reset_token.token}"

    subject = "Réinitialisation de votre mot de passe"
    message = f"""
Bonjour {user.first_name},

Vous avez demandé la réinitialisation de votre mot de passe.
Cliquez sur le lien ci-dessous pour en définir un nouveau :

{reset_link}

Ce lien expirera dans 15 minutes.

Si vous n’êtes pas à l’origine de cette demande, ignorez cet email.

Cordialement,
L'équipe Calm Adventure Tours
"""

    try:
        from_email = f'Calm Adventure Tours <{settings.DEFAULT_FROM_EMAIL}>'
        send_mail(
            subject=subject,
            message=message,
            recipient_list=[email],
            from_email=from_email,
            fail_silently=False,
        )
        logger.info(f"Email de réinitialisation envoyé à {email} depuis {from_email}")
    except Exception as e:
        logger.error(f"Échec de l'envoi de l'email de réinitialisation : {e}")
        return Response({'error': 'Impossible d’envoyer l’email. Veuillez réessayer.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'message': 'Un email de réinitialisation a été envoyé.'})


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    token = request.data.get('token')
    new_password = request.data.get('new_password')

    if not token or not new_password:
        return Response({'error': 'Tous les champs sont requis.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        reset_entry = PasswordResetToken.objects.get(token=token)
        if not reset_entry.is_valid():
            return Response({'error': 'Le lien de réinitialisation a expiré.'}, status=status.HTTP_400_BAD_REQUEST)

        user = reset_entry.user
        user.set_password(new_password)
        user.save()

        PasswordResetToken.objects.filter(user=user).delete()

        return Response({'message': 'Mot de passe réinitialisé avec succès.'})

    except PasswordResetToken.DoesNotExist:
        return Response({'error': 'Lien invalide.'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Seul l'admin peut créer/modifier/supprimer
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
            user = self.request.user
            if user.role != 'admin':
                from rest_framework.permissions import IsAdminUser
                self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()