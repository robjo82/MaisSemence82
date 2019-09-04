from django.contrib import admin
from .models import PlaceOfWork

class PlaceOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'placeofwork',
        )

    list_filter = (
        'user',
        'placeofwork',
        )

    ordering = (
        'placeofwork',
        'user',
        )

    search_fields = (
        'placeofwork',
        'user',
        )

admin.site.register(PlaceOfWork, PlaceOfWorkAdmin)