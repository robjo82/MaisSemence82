from django.shortcuts import render, redirect
from .forms import UserForm, UserExtentionForm

# Create your views here.
"""def registration (request):
    form = UserForm(request.POST or None)
    form2 = UserExtentionForm(request.POST or None, request.FILES)
    envoi = False
    if form.is_valid() and form2.is_valid():
        user = form.save()
        user_extention = form2.save(commit = False)
        user_extention.user = user
        user_extention.save()
        envoi = True

    return render (request, 'registration/registration.html', locals())"""

def registration (request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        form2 = UserExtentionForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user_extention = form2.save(commit = False)
            user_extention.user = user
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