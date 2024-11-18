from django import forms

from event_planner.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        super().clean()
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        if start_time and end_time and start_time > end_time:
            raise forms.ValidationError("L'heure de fin doit être ultérieure à l'heure de début.")

        return self.cleaned_data