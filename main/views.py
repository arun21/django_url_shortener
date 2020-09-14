from django.shortcuts import render


# Create your views here.

def Make(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html', {'name': "Arun"})
