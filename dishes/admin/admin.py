from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dishes.models import Dish


@admin.register(Dish)
class DishModelAdmin(admin.ModelAdmin):
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
                'fields': ('name',)
            }
        ),
    )
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
