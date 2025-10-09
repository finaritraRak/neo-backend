from django import forms
from django.contrib import admin
from .widgets import MultilingualJSONWidget


class AutoMultilingualAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if hasattr(field, 'widget') and isinstance(field.widget, forms.widgets.Input):
                model_field = self._meta.model._meta.get_field(field_name)
                if getattr(model_field, 'get_internal_type', lambda: None)() == 'JSONField':
                    self.fields[field_name].widget = MultilingualJSONWidget()
                    self.fields[field_name].required = False


class AutoMultilingualAdmin(admin.ModelAdmin):
    form = AutoMultilingualAdminForm
