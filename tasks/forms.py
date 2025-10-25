from django import forms
from .models import TestsTodo

EDITABLE_FIELDS = [
    # add right there fields which have to be edit
    'testname',
    'underlying',
    'startingfunds',
    'allocationpercentage',
    'maxopentrades',
]

class TaskForm(forms.ModelForm):
    class Meta:
        model = TestsTodo
        fields = EDITABLE_FIELDS
