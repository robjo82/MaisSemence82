from django import forms
from .models import UserExtention
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            )

class UserExtentionForm(forms.ModelForm):
    class Meta:
        model = UserExtention
        exclude = ('user',)
    