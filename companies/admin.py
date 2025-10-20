# companies/admin.py
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'country', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('name', 'domain')
    ordering = ('name',)
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('name', 'domain', 'country')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)