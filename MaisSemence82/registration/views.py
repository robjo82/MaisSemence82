from django.shortcuts import render, redirect
from .forms import UserForm, UserExtentionForm
from HoursDeclaration.models import HoursDeclaration
from placeofwork.models import PlaceOfWork

def registration (request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        form2 = UserExtentionForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user_extention = form2.save(commit = False)
            user_extention.user = user
            hours_declaration_user = HoursDeclaration.objects.create(user = user)
            placeofwork_user = PlaceOfWork.objects.create(user = user)
            user_extention.save()
            return redirect('index')
    else:
        form = UserForm()
        form2 = UserExtentionForm()
        
    return render (
        request,
        'registration/registration.html',
        {'form': form, 'form2': form2}
    )