from django import forms
from django.forms import widgets
from webapp.models import TrackerType, TrackerStatus

class TrackerForm(forms.Form):
    summary = forms.CharField(max_length=200, required=False, label='Kratkoe opisanie')
    description = forms.CharField(max_length=3000, required=True, label='Polnoe opisanie', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=TrackerStatus, label='Status')
    type = forms.ChoiceField(choices=TrackerType, label='Tip')
