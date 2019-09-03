from django.shortcuts import render

def placeofwork(request):
    return render(request, 'placeofwork/placeofwork.html', locals())