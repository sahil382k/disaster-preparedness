from django import forms
from .models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['message', 'target_audience', 'geo_fence']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }