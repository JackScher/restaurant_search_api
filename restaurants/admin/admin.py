from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        (
            _('System Attributes'),
            {
                'fields': ('id',)
            }
        ),
        (
            _('Properties'),
            {
                'fields': ('name', 'address', 'phone', 'email')
            }
        ),
    )
    list_display = ('name', 'address',)
    search_fields = ('name', 'address')
    ordering = ('name',)
