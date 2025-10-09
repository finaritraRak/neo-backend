# contacts/models.py
from django.db import models

class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    travelers = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
