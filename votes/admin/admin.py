from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from votes.models import Vote


@admin.register(Vote)
class VoteModelAdmin(admin.ModelAdmin):
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
                'fields': ('employee', 'menu')
            }
        ),
    )
    list_display = ('employee', 'menu')
    search_fields = ('employee', 'menu')
    ordering = ('employee', 'menu')
