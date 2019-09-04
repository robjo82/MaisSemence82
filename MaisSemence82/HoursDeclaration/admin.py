from django.contrib import admin
from .models import HoursDeclaration

class HoursDeclarationAdmin (admin.ModelAdmin):
    list_display = (
        'user',
        'hours_number',
        )

    list_filter = (
        'user',
        'hours_number'
        )

    ordering = (
        'hours_number',
         'user'
         )

    search_fields = (
        'user',
        'hours_number',
        )

admin.site.register (HoursDeclaration, HoursDeclarationAdmin)
