# energy_data/models.py
from django.db import models
from sites.models import Site

class EnergyReading(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='readings')
    timestamp = models.DateTimeField(db_index=True)  

    # Données brutes
    total_load_kwh = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)  # Total Compteurs Load
    genset_kwh = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)      # Compteur GE
    pv_production_kwh = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)  # PV Production
    battery_kwh = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)       # Battery
    pv_theoretical_kwh = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True) # Production théorique

    # Métadonnées
    is_valid = models.BooleanField(default=True)   
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        unique_together = ('site', 'timestamp')
        indexes = [
            models.Index(fields=['site', '-timestamp']),
        ]

    def __str__(self):
        return f"{self.site.name} @ {self.timestamp}"