from django import forms
from .widgets import MultiLanguageJSONWidget


class MultiLanguageJSONField(forms.JSONField):
    def __init__(self, *args, **kwargs):
        self.languages = kwargs.pop('languages', None)
        kwargs['widget'] = MultiLanguageJSONWidget(languages=self.languages)
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        return value or {}
