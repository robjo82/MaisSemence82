from django.shortcuts import render
from .forms import UserForm, UserExtentionForm

# Create your views here.
def registration (request):
    form = UserForm(request.POST or None)
    form2 = UserExtentionForm(request.POST or None)
    envoi = False
    if form.is_valid() and form2.is_valid():
        user = form.save()
        user_extention = form2.save(commit = False)
        user_extention.user = user
        user_extention.save()
        envoi = True

    return render (request, 'registration/registration.html', locals())