# sites/admin.py
from django.contrib import admin
from .models import Site

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'topology', 'location', 'is_active', 'created_at')
    list_filter = ('company', 'topology', 'is_active', 'created_at')
    search_fields = ('name', 'location', 'company__name')
    list_editable = ('is_active',)
    ordering = ('company', 'name')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'topology')
        }),
        ('Localisation', {
            'fields': ('location',),
            'classes': ('collapse',)
        }),
        ('Statut', {
            'fields': ('is_active',),
        }),
    )