# apps/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets
from datetime import timedelta, datetime

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('technicien', 'Technicien'),
        ('client', 'Client'),
    ]

    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('inactive', 'Inactif'),
        ('pending', 'En attente'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')  # Changé à 20 pour technicien
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(32)
        if not self.expires_at:
            self.expires_at = datetime.now() + timedelta(minutes=15)
        super().save(*args, **kwargs)

    def is_valid(self):
        return datetime.now() < self.expires_at.replace(tzinfo=None)

    def __str__(self):
        return f"{self.user.email} - {self.token}"