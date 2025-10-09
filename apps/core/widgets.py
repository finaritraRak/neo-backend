from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
import json
import uuid

class MultilingualJSONInput(forms.Widget):
    def __init__(self, attrs=None, field_name=''):
        self.languages = getattr(settings, 'PROJECT_LANGUAGES', ['fr', 'en'])
        self.field_name = field_name
        super().__init__(attrs)

    def value_from_datadict(self, data, files, name):
        return {
            lang: data.get(f'{name}_{lang}', '').strip()
            for lang in self.languages
        }

    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = {}
        value = value or {}

        uid = uuid.uuid4().hex[:6]
        html = ''
        toggle_buttons = ''

        for lang in self.languages:
            field_id = f'id_{name}_{lang}_{uid}'
            lang_label = lang.upper()
            val = value.get(lang, '')
            visible = 'block' if lang == 'fr' else 'none'

            is_rich = self.field_name in ['content', 'meta_description', 'requirements']
            if is_rich:
                input_html = f'<textarea name="{name}_{lang}" id="{field_id}" rows="6" style="width:100%;">{val}</textarea>'
            else:
                input_html = f'<input type="text" name="{name}_{lang}" value="{val}" id="{field_id}" style="width:100%; padding:6px; border:1px solid #ccc; border-radius:6px;" />'

            html += f'''
                <div id="wrap_{field_id}" style="margin-bottom:12px; display:{visible};">
                    <label for="{field_id}" style="font-weight:bold; display:block; margin-bottom:4px;">{lang_label}</label>
                    {input_html}
                    <button type="button" class="lang-remove-btn" onclick="toggleFieldVisibility('{field_id}', this)" style="display:{'block' if lang != 'fr' else 'none'};">
                        <span style="margin-right:4px;">−</span> Masquer {lang_label}
                    </button>
                </div>
            '''

            if lang != 'fr':
                toggle_buttons += f'''
                    <button type="button" class="lang-add-btn" onclick="toggleFieldVisibility('{field_id}', this)">
                        <span style="margin-right:4px;">＋</span> Ajouter {lang_label}
                    </button>
                '''

        html += f'''
            <div style="margin-bottom:15px;">{toggle_buttons}</div>

            <style>
                .lang-add-btn {{
                    background-color: #2563eb;  /* Blue */
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 6px 12px;
                    margin-right: 8px;
                    font-size: 13px;
                    cursor: pointer;
                }}
                .lang-add-btn:hover {{
                    background-color: #1d4ed8;
                }}

                .lang-remove-btn {{
                    background-color: #dc2626;  /* Red */
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 4px 10px;
                    margin-top: 8px;
                    font-size: 12px;
                    cursor: pointer;
                }}
                .lang-remove-btn:hover {{
                    background-color: #b91c1c;
                }}
            </style>

            <script>
                function toggleFieldVisibility(fieldId, btn) {{
                    const wrapper = document.getElementById("wrap_" + fieldId);
                    const isVisible = wrapper.style.display === "block";
                    wrapper.style.display = isVisible ? "none" : "block";

                    if (btn.classList.contains("lang-add-btn")) {{
                        btn.style.display = "none";
                        const hideBtn = wrapper.querySelector(".lang-remove-btn");
                        if (hideBtn) hideBtn.style.display = "block";
                    }} else if (btn.classList.contains("lang-remove-btn")) {{
                        const addBtn = document.querySelector(".lang-add-btn[onclick*='" + fieldId + "']");
                        if (addBtn) addBtn.style.display = "inline-block";
                        btn.style.display = "none";
                    }}
                }}
            </script>
        '''

        return mark_safe(html)
