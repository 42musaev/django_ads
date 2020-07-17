from django import forms
from .models import Applications


class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['user_name', 'phone', 'ads']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'request__input'}),
            'phone': forms.TextInput(attrs={'class': 'request__input'}),
        }
