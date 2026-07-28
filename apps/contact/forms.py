from django import forms
from .models import ContactMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column, HTML

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "message"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. John Doe'}),
            'phone': forms.TextInput(attrs={'placeholder': 'e.g. +1 234 567 8900'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your message here...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Modern, flat styling without shadows
        field_css = 'bg-slate-50 border-slate-200 text-slate-900 rounded-2xl focus:ring-4 focus:ring-indigo-900/10 focus:border-indigo-900 focus:bg-white px-5 py-4 transition-all duration-300 hover:border-indigo-400 hover:bg-slate-100 hover:shadow-md shadow-sm outline-none'
        self.helper.layout = Layout(
            Row(
                Column(Field('name', css_class=field_css), css_class='form-group col-span-1'),
                Column(Field('phone', css_class=field_css), css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-8 mb-4'
            ),
            Column(Field('message', css_class=field_css), css_class='mb-4'),
            HTML('<div class="mt-8 mb-4">'),
            Submit('submit', 'Send Message', css_class='w-full bg-indigo-900 hover:bg-indigo-800 text-white font-bold py-3 px-8 rounded-xl transition-all cursor-pointer text-base tracking-wide'),
            HTML('</div>')
        )
