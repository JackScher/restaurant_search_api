from django.contrib import admin
from django.forms import ModelForm, ModelMultipleChoiceField
from menus.models import Menu


class MenuAdminForm(ModelForm):
    persons = ModelMultipleChoiceField(
        queryset=Menu.dishes.field.related_model.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple(
            "dishes",
            is_stacked=False
        ),
        required=False,
    )
