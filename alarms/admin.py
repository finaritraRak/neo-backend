# alarms/admin.py
from django.contrib import admin
from .models import Alarm, AlarmType

@admin.register(Alarm)
class AlarmAdmin(admin.ModelAdmin):
    list_display = (
        'alarm_type',
        'site',
        'is_active',
        'severity',
        'triggered_at',
        'resolved_at'
    )
    list_filter = (
        'site__company',
        'site',
        'alarm_type',
        'is_active',
        'severity',
        'triggered_at'
    )
    search_fields = (
        'site__name',
        'site__company__name',
        'description'
    )
    list_editable = ('is_active',)
    date_hierarchy = 'triggered_at'
    ordering = ('-triggered_at',)
    list_per_page = 50

    fieldsets = (
        (None, {
            'fields': ('site', 'reading', 'alarm_type', 'description')
        }),
        ('Statut & Gravité', {
            'fields': ('is_active', 'severity', 'triggered_at', 'resolved_at')
        }),
    )
    readonly_fields = ('triggered_at',)