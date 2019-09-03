from django import forms
from django.contrib.auth.models import User 

class HoursDeclarationForm(forms.Form):
    number_of_hours = forms.FloatField(required=True)
    presence = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )