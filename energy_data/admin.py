# energy_data/admin.py
from django.contrib import admin
from .models import EnergyReading

@admin.register(EnergyReading)
class EnergyReadingAdmin(admin.ModelAdmin):
    list_display = (
        'site',
        'timestamp',
        'total_load_kwh',
        'pv_production_kwh',
        'genset_kwh',
        'battery_kwh',
        'is_valid',
        'created_at'
    )
    list_filter = (
        'site__company',
        'site',
        'is_valid',
        'timestamp'
    )
    search_fields = (
        'site__name',
        'site__company__name'
    )
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    list_per_page = 50

    fieldsets = (
        (None, {
            'fields': ('site', 'timestamp', 'is_valid')
        }),
        ('Données énergétiques (kWh)', {
            'fields': (
                'total_load_kwh',
                'genset_kwh',
                'pv_production_kwh',
                'battery_kwh',
                'pv_theoretical_kwh'
            ),
            'classes': ('collapse',)
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)