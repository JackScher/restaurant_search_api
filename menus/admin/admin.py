from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .forms import MenuAdminForm
from menus.models import Menu


@admin.register(Menu)
class MenuModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    form = MenuAdminForm
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
                'fields': ('price', 'restaurant', 'dishes')
            }
        ),
    )
    list_display = ('restaurant', 'date', 'related_dishes', 'price')
    search_fields = ('date',)
    ordering = ('date',)
