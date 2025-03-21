from django import forms
from .models import XPEntry


class XPEntryForm(forms.ModelForm):
    class Meta:
        model = XPEntry
        fields = ['user', 'activity', 'xp_points']
