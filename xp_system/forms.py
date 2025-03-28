from django import forms
from .models import XPEntry

# XP form based on the updated XPEntry model
class XPForm(forms.ModelForm):
    class Meta:
        model = XPEntry
        fields = ['user', 'category', 'amount']
