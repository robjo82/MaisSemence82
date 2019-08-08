from django.contrib import admin
from .models import UserExtention

class UserExtentionAdmin (admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'postal_code',
        'town',
        'id_card_recto',
        'id_card_verso',
        'vital_card',
        'hours_number',
        )

    list_filter = (
        'user',
        'phone_number',
        'postal_code',
        'town',
        'id_card_recto',
        'id_card_verso',
        'vital_card',
        'hours_number',
        )

    ordering = ('user',)

    search_fields = (
        'user',
        'phone_number',
        'postal_code',
        'town',
        'id_card_recto',
        'id_card_verso',
        'vital_card',
        'hours_number',
        )

admin.site.register (UserExtention, UserExtentionAdmin)