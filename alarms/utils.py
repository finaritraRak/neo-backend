# alarms/utils.py
import pandas as pd
from apps.energy_data.models import EnergyReading
from apps.alarms.models import Alarm, AlarmType

def detect_meter_disconnection(site_id):
    """Détecte les compteurs déconnectés (valeurs NULL)"""
    readings = EnergyReading.objects.filter(
        site_id=site_id,
        timestamp__gte=pd.Timestamp.now(tz='UTC') - pd.Timedelta(hours=24)
    ).values('id', 'timestamp', 'pv_production_kwh', 'battery_kwh', 'genset_kwh')

    for r in readings:
        if r['pv_production_kwh'] is None or r['battery_kwh'] is None:
            Alarm.objects.get_or_create(
                site_id=site_id,
                reading_id=r['id'],
                alarm_type=AlarmType.METER_DISCONNECTED,
                defaults={'description': 'Donnée manquante détectée', 'is_active': True}
            )

def detect_pv_cutting(site_id):
    """Implémente la logique fournie par le client"""
    from .pv_cutting_logic import detect_ecretage  # tu mets le code client ici

    df = pd.DataFrame(list(
        EnergyReading.objects.filter(site_id=site_id).values(
            'id', 'timestamp',
            PV_theorique=models.F('pv_theoretical_kwh'),
            PV_reel=models.F('pv_production_kwh'),
            Load=models.F('total_load_kwh'),
            Genset=models.F('genset_kwh')
        )
    ))

    if df.empty:
        return

    df = detect_ecretage(df)

    for _, row in df[df['Ecretage_PV']].iterrows():
        Alarm.objects.get_or_create(
            site_id=site_id,
            reading_id=row['id'],
            alarm_type=AlarmType.PV_CUTTING,
            defaults={
                'description': f"Écrêtage détecté – Type: {row['Type_Ecretage']}",
                'is_active': True
            }
        )