# contacts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import get_user_model
from django.apps import apps
from .models import ContactRequest
import logging

logger = logging.getLogger(__name__)

NOTIFICATIONS_ENABLED = apps.is_installed('notifications')
User = get_user_model()

class ContactRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
          
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            if not name or not email:
                return Response(
                    {'error': 'Name and email are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

          
            contact = ContactRequest.objects.create(
                name=name,
                email=email,
                phone=data.get('phone', '').strip(),
                destination=data.get('destination', '').strip(),
                duration=data.get('duration', '').strip(),
                travelers=data.get('travelers', '').strip(),
                budget=data.get('budget', '').strip(),
                message=data.get('message', '').strip(),
            )

           
            email_subject = f"Nouveau message de contact : {name}"

           
            email_body = f"""
Nouvelle demande de contact reçue via le site Calm Adventure Tours.

Nom complet : {name}
Email : {email}
Téléphone : {data.get('phone') or 'Non fourni'}
Destination souhaitée : {data.get('destination') or 'Non spécifiée'}
Durée du séjour : {data.get('duration') or 'Non spécifiée'}
Nombre de voyageurs : {data.get('travelers') or 'Non spécifié'}
Budget estimé : {data.get('budget') or 'Non spécifié'}
Message :
{data.get('message') or 'Aucun message'}

Envoyé depuis le formulaire de contact général du site.
            """.strip()

           
            from_email_display = f"{name} <{settings.DEFAULT_FROM_EMAIL}>"

           
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=from_email_display,
                to=['hello@calm-adventure-tours.com'],  
                reply_to=[email],
            )

           
            email.extra_headers = {
                'Reply-To': f"{name} <{email}>",
                'X-Priority': '3',
                'X-Mailer': 'CalmAdventureTours Backend',
                'Precedence': 'bulk',
            }

         
            email.send(fail_silently=False)

            logger.info(f"Email de contact envoyé avec succès par {name} ({email})")

           
            if NOTIFICATIONS_ENABLED:
                try:
                  
                    from notifications.models import Notification  

                    admins = User.objects.filter(is_staff=True)
                    if not admins.exists():
                        logger.warning("[NOTIFICATIONS] Aucun admin trouvé. Notification non créée.")
                    else:
                        for admin in admins:
                            Notification.objects.create(
                                recipient=admin,
                                actor=f"{name} ({email})",
                                verb="a envoyé un nouveau message de contact",
                                target_url="/admin-panel/content#contacts",
                                notification_type="contact"
                            )
                        logger.info(f"[NOTIFICATIONS] {admins.count()} notification(s) créée(s) pour le contact de {name}")
                except Exception as e:
                    logger.error(f"[NOTIFICATIONS] Échec de création pour {name}: {str(e)}")

            return Response({'success': True}, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Erreur lors du traitement du formulaire de contact : {str(e)}")
            return Response(
                {'error': 'Une erreur est survenue. Veuillez réessayer plus tard.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )