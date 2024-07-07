# records/forms.py
from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'start_time', 'activity_type']  # Exclude end_time and color