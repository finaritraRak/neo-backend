# settings/models.py
from django.db import models
from django.conf import settings

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='')
    site_description = models.TextField(blank=True, default='')
    contact_email = models.EmailField(blank=True, default='')
    timezone = models.CharField(max_length=50, default='Europe/Paris')
    language = models.CharField(max_length=10, default='fr')
    theme = models.CharField(max_length=20, default='light')
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=False)
    weekly_reports = models.BooleanField(default=True)
    two_factor_auth = models.BooleanField(default=False)
    session_timeout = models.IntegerField(default=30)
    password_expiry = models.IntegerField(default=90)

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"Paramètres du site ({self.site_name})"

# Étendre le modèle User avec un profil
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, default='')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    def __str__(self):
        return f"Profil de {self.user.username}"