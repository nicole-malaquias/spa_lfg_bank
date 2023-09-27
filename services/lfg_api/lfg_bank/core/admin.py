from django import forms
from django.contrib import admin

from .models import ConfigurableFields, Proposal

class ConfigurableFieldsForm(forms.ModelForm):
    class Meta:
        model = ConfigurableFields
        fields = '__all__'

    active_fields = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(f.name, f.name) for f in Proposal._meta.fields if f.name != 'id']
    )

class ConfigurableFieldsAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_active_fields']
    form = ConfigurableFieldsForm

    def get_active_fields(self, obj):
        return ", ".join(obj.active_fields)
    get_active_fields.short_description = 'Active Fields'

admin.site.register(ConfigurableFields, ConfigurableFieldsAdmin)

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Proposal._meta.fields]


