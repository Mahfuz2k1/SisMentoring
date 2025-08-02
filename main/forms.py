

from django import forms
from .models import MenteeApplication

class MenteeApplicationForm(forms.ModelForm):
    class Meta:
        model = MenteeApplication
        fields = ['name', 'email', 'whatsapp', 'profession', 'country', 'district', 'address', 'description', 'problems', 'goal_6month']
        labels = {
            'description': 'Describe yourself and your profession:',
            'problems': 'Problems you want to overcome:',
            'goal_6month': 'Your Target in Next 6 Months',
            'whatsapp': 'WhatsApp Number'
        }
        widgets = {
            'whatsapp': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'problems': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'goal_6month': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
