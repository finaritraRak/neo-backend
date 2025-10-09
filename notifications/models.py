# notifications/models.py
from django.db import models
from django.conf import settings 
from django.utils import timezone

class Notification(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    actor = models.CharField(max_length=255)
    verb = models.CharField(max_length=255)
    target_url = models.URLField(blank=True, null=True)
    notification_type = models.CharField(max_length=50, choices=[
        ('contact', 'Formulaire de contact'),
        ('booking', 'Réservation'),
        ('blog_comment', 'Commentaire blog'),
        ('user_registered', 'Nouvel utilisateur'),
        ('custom', 'Personnalisé'),
    ])
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.actor} {self.verb}"