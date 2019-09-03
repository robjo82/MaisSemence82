from django.shortcuts import render
from .forms import HoursDeclarationForm
from django.contrib.auth.models import User 
from registration.models import UserExtention


def hours_declaration (request):
    form = HoursDeclarationForm(request.POST or None)

    if form.is_valid():
        number_of_hours = form.cleaned_data['number_of_hours']
        presence = form.cleaned_data['presence']

        for username in presence :
            user = UserExtention.objects.get(user = username)
            user.hours_number += number_of_hours
            user.save()
    return render (
        request,
        'HoursDeclaration/hours_declaration.html'
        , locals()
        )