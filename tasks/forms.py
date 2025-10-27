from django import forms
from .models import TestsTodo

class TaskForm(forms.ModelForm):
    class Meta:
        model = TestsTodo
        exclude = ['testid']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'status' in self.fields:
            self.fields['status'].disabled = True
