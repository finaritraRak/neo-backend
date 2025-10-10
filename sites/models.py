# sites/models.py
from django.db import models
from companies.models import Company

class Site(models.Model):
    TOPOLOGY_CHOICES = [
        ('solar_battery', 'Panneau solaire + Batterie'),
        ('solar_se_battery', 'Panneau solaire + SE + Batterie'),
        ('solar_generator', 'Panneau solaire + Groupe électrogène'),
        ('jirama', 'Jirama (ou fournisseur national)'),
    ]

    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sites')
    topology = models.CharField(max_length=50, choices=TOPOLOGY_CHOICES)
    location = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('company', 'name')

    def __str__(self):
        return f"{self.name} ({self.company.name})"