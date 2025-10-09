from django import forms
from django.db.models import JSONField
from .widgets import MultilingualJSONInput

class AutoMultilingualForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            model_field = self._meta.model._meta.get_field(field_name)
            if isinstance(model_field, JSONField):
                self.fields[field_name].widget = MultilingualJSONInput(field_name=field_name)
                self.fields[field_name].required = False
