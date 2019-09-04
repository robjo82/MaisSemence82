from django.contrib import admin
from .models import UserExtention

class UserExtentionAdmin (admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'postal_code',
        'town',
        'address',
        'id_card_recto',
        'id_card_verso',
        'vital_card',
        )

    list_filter = (
        'user',
        'phone_number',
        'postal_code',
        'town',
        'address',
        'id_card_recto',
        'id_card_verso',
        'vital_card',
        )

    ordering = ('user',)

    search_fields = (
        'user',
        'phone_number',
        'postal_code',
        'town',
        'address',
        'id_card_recto',
        'id_card_verso',
        'vital_card',
        )

admin.site.register (UserExtention, UserExtentionAdmin)