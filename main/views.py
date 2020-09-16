from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortener import shortener

# Create your views here.

def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def Make(request):
    form = UrlForm(request.POST)
    url = ''
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            url = shortener().issue_token()
            NewUrl.short_url = url
            NewUrl.save()
        else:
            form = UrlForm()
            url = "Invalid URL"
    return render(request, 'home.html', {'form':form, 'url': url})


def About(request):
    return render(request, 'about.html', {'name': 'Arun'})
