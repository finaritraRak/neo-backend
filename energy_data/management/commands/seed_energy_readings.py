# energy_data/management/commands/seed_energy_readings.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from energy_data.models import EnergyReading
from sites.models import Site
import random
from datetime import timedelta

class Command(BaseCommand):
    help = "Génère des données fictives pour EnergyReading"

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help="Nombre de lectures à générer par site"
        )
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help="Nombre de jours dans le passé à couvrir"
        )

    def handle(self, *args, **options):
        count = options['count']
        days = options['days']

        sites = Site.objects.all()
        if not sites.exists():
            self.stdout.write(self.style.ERROR("Aucun site trouvé. Veuillez en créer au moins un."))
            return

        start_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days)

        for site in sites:
            self.stdout.write(f"Génération de {count} lectures pour le site {site.name}...")
            for i in range(count):
                timestamp = start_date + timedelta(
                    minutes=random.randint(0, days * 24 * 60 - 1)
                )
                EnergyReading.objects.get_or_create(
                    site=site,
                    timestamp=timestamp,
                    defaults={
                        'total_load_kwh': round(random.uniform(10, 500), 3),
                        'genset_kwh': round(random.uniform(0, 300), 3),
                        'pv_production_kwh': round(random.uniform(0, 400), 3),
                        'battery_kwh': round(random.uniform(-100, 100), 3),  # peut être négatif (décharge)
                        'pv_theoretical_kwh': round(random.uniform(0, 450), 3),
                        'is_valid': random.choice([True, True, True, False]),  # 25% invalides
                    }
                )
        self.stdout.write(self.style.SUCCESS("Données fictives générées avec succès !"))