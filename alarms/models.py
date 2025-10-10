# alarms/models.py
from django.db import models
from sites.models import Site
from energy_data.models import EnergyReading

class AlarmType(models.TextChoices):
    METER_DISCONNECTED = 'meter_disconnected', 'Compteur déconnecté'
    PV_CUTTING = 'pv_cutting', 'Écrêtage PV'
    BATTERY_FAULT = 'battery_fault', 'Anomalie batterie'
    LOW_PRODUCTION = 'low_production', 'Production PV anormalement basse'
    OVERLOAD = 'overload', 'Surcharge réseau'

class Alarm(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='alarms')
    reading = models.ForeignKey(EnergyReading, on_delete=models.SET_NULL, null=True, blank=True)
    alarm_type = models.CharField(max_length=50, choices=AlarmType.choices)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)  # active = non résolue
    severity = models.IntegerField(default=1)  # 1=info, 2=warning, 3=critical
    triggered_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-triggered_at']

    def __str__(self):
        return f"{self.get_alarm_type_display()} - {self.site.name}"