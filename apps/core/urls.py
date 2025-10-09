# apps/core/urls.py
from django.urls import path
from .views import api_root, ContactMessageCreateView, NewsletterSubscribeView  # ✅ importer api_root ici

urlpatterns = [
    path('', api_root, name='api-root'),  # ✅ utiliser directement api_root
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
    path('newsletter/', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
]
