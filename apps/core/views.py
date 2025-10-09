from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import ContactMessage, Newsletter
from .serializers import ContactMessageSerializer, NewsletterSerializer
from django.core.mail import send_mail
from django.conf import settings


@method_decorator(csrf_exempt, name='dispatch')
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # 🔔 Envoi de l'email
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']

        full_message = f"""
        Nouveau message de contact via le site Lynkevo :

        Nom : {name}
        Email : {email}
        Sujet : {subject}

        Message :
        {message}
        """

        send_mail(
            subject=f"[Contact Lynkevo] {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['hello@gmail.com'],
            fail_silently=False
        )

        return Response(
            {"message": "Message sent and email sent successfully!"},
            status=status.HTTP_201_CREATED
        )
        
class NewsletterSubscribeView(generics.CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Newsletter.objects.filter(email=email).exists():
            return Response(
                {"message": "Email already subscribed!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Successfully subscribed to newsletter!"},
            status=status.HTTP_201_CREATED
        )


@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Bienvenue sur l'API Lynkevo ✨",
        "routes": {
            "contact": "/api/contact/",
            "newsletter": "/api/newsletter/",
            "blog": "/api/blog/",
            "seo": "/api/seo/",
            "services": "/api/services/",
            "testimonials": "/api/testimonials/",
            "team": "/api/team/",
            "analytics": "/api/analytics/",
        }
    })
