# contacts/urls.py
from django.urls import path
from .views import ContactRequestView

urlpatterns = [
    path("request/", ContactRequestView.as_view(), name="contact-request"),
]
