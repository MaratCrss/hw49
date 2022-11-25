from django import forms
from django.forms import widgets, ValidationError
from webapp.models import TrackerType, TrackerStatus, Tracker



class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': widgets.CheckboxSelectMultiple,
            'type': widgets.CheckboxSelectMultiple
        }

        error_messages = {
            'description': {
                'required': 'Napishi chto-nibud tut'
            }
        }

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 5:
            self.add_error('summary', ValidationError('Summary ne menshe %(length)d simvolov!', code='too_short', params={'length': 5}))
        return summary


    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 20:
            self.add_error('description', ValidationError('Description ne menee %(length)d simvolov!', code='too_short', params={'length': 20}))
        return description



    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data.get('description', ''):
            raise ValidationError('Summary i description ne doljny byt odinakovymi')