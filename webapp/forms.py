from django import forms
from django.forms import widgets
from webapp.models import TrackerType, TrackerStatus

class TrackerForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Kratkoe opisanie')
    description = forms.CharField(max_length=3000, required=False, label='Polnoe opisanie', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=TrackerStatus.objects.all(), required=True, label='Status')
    type = forms.ModelChoiceField(queryset=TrackerType.objects.all(), required=True, label='Tip')
